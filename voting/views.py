from django.shortcuts import render

# Create your views here.
# views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Candidate, Vote
from django.contrib.auth.decorators import login_required
import hashlib
import datetime

def generate_blockchain_hash(vote_data):
    """
    Simulates generating a blockchain transaction hash.
    This should be replaced with actual blockchain integration.
    """
    data = f"{vote_data['user_id']}-{vote_data['candidate_id']}-{datetime.datetime.now()}"
    return hashlib.sha256(data.encode()).hexdigest()

@login_required
def cast_vote(request, candidate_id):
    user = request.user
    
    # Ensure user has not voted before
    if Vote.objects.filter(user=user).exists():
        return JsonResponse({'error': 'You have already voted'}, status=403)
    
    # Get the candidate the user is voting for
    try:
        candidate = Candidate.objects.get(pk=candidate_id)
    except Candidate.DoesNotExist:
        return JsonResponse({'error': 'Candidate not found'}, status=404)
    
    # Prepare vote data for blockchain hash generation
    vote_data = {
        'user_id': user.id,
        'candidate_id': candidate_id
    }
    
    # Generate blockchain hash
    blockchain_hash = generate_blockchain_hash(vote_data)
    
    # Record the vote in the database
    vote = Vote.objects.create(
        user=user,
        candidate=candidate,
        blockchain_hash=blockchain_hash,
        timestamp=timezone.now()
    )
    
    return JsonResponse({
        'message': 'Vote successfully cast!',
        'candidate': candidate.name,
        'blockchain_hash': blockchain_hash
    })

@login_required
def view_candidates(request):
    candidates = Candidate.objects.all()
    return render(request, 'voting/candidates.html', {'candidates': candidates})

@login_required
def view_vote(request):
    user = request.user
    
    try:
        vote = Vote.objects.get(user=user)
        return JsonResponse({
            'candidate': vote.candidate.name,
            'party': vote.candidate.party,
            'blockchain_hash': vote.blockchain_hash,
            'timestamp': vote.timestamp
        })
    except Vote.DoesNotExist:
        return JsonResponse({'message': 'You have not voted yet'}, status=404)
