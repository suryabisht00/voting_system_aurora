
import hashlib
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Candidate, Vote
from user_management.models import User  # Import the User model for user verification
from django.utils import timezone

# Helper function to create blockchain hash
def generate_blockchain_hash(user, candidate):
    """
    Generates a unique blockchain hash for the vote.
    :param user: User object casting the vote
    :param candidate: Candidate object being voted for
    :return: Unique blockchain hash (SHA256)
    """
    vote_data = f'{user.id}{candidate.id}{timezone.now()}'
    return hashlib.sha256(vote_data.encode()).hexdigest()

# View to display voting page
@login_required  # Ensure the user is logged in and verified
def voting_page(request):
    """
    Displays the list of candidates to the user for voting.
    """
    if request.method == 'GET':
        # Fetch all candidates to display on the voting page
        candidates = Candidate.objects.all()
        return render(request, 'voting_main_page.html', {'candidates': candidates})

# View to handle voting process
@login_required
def cast_vote(request):
    """
    Handles the vote casting process and stores the vote in the blockchain.
    """
    if request.method == 'POST':
        candidate_id = request.POST.get('candidate')  # Get candidate ID from form submission
        candidate = get_object_or_404(Candidate, id=candidate_id)  # Fetch candidate

        # Ensure the user hasn't already voted
        if Vote.objects.filter(user=request.user).exists():
            return HttpResponse('You have already voted!', status=400)

        # Generate blockchain hash for the vote
        blockchain_hash = generate_blockchain_hash(request.user, candidate)

        # Create a new Vote object and save it
        vote = Vote.objects.create(
            user=request.user,
            candidate=candidate,
            blockchain_hash=blockchain_hash
        )

        # Redirect to a success page after voting
        return redirect('voting:after_successful_voting')

    # If it's not a POST request, redirect back to the voting page
    return redirect('voting:voting_page')

# View for the successful voting page
@login_required
def after_successful_voting(request):
    """
    Renders the page after successful voting.
    """
    return render(request, 'after_successful_voting.html')
