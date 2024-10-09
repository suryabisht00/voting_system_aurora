from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_management.models import Candidate, CitizenData
from aadhaar_voter_card.models import AadhaarVerification
from voting.models import VotingStatus

# Home Page View
def home(request):
    return render(request, 'home_page.html')

# Admin Panel View (Redirecting to Django's Admin Interface)
@login_required
def admin_panel(request):
    return redirect('/admin/')

# Vote Status View
@login_required
def vote_status(request):
    # Fetch the voting status for the logged-in citizen
    citizen = CitizenData.objects.filter(mobile=request.user.username).first()
    if citizen:
        try:
            voting_status = VotingStatus.objects.get(citizen=citizen)
        except VotingStatus.DoesNotExist:
            voting_status = None
    else:
        voting_status = None

    return render(request, 'vote_status.html', {'voting_status': voting_status})

# Voting View
@login_required
def vote(request):
    if request.method == 'POST':
        # Assuming you have a simple form for citizens to vote for a candidate
        candidate_id = request.POST.get('candidate_id')
        citizen = CitizenData.objects.filter(mobile=request.user.username).first()

        if candidate_id and citizen:
            candidate = Candidate.objects.get(id=candidate_id)
            candidate.vote_count += 1
            candidate.save()

            # Update voting status
            VotingStatus.objects.update_or_create(
                citizen=citizen,
                defaults={'status': 'voted'}
            )
            return redirect('vote_status')

    candidates = Candidate.objects.all()
    return render(request, 'vote.html', {'candidates': candidates})

# Result View
@login_required
def result(request):
    # Fetch all candidates and their vote counts
    candidates = Candidate.objects.all().order_by('-vote_count')
    return render(request, 'result.html', {'candidates': candidates})
