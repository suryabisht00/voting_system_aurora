from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_management.models import Candidate, CitizenData
from aadhaar_voter_card.models import AadhaarVerification
from voting.models import VotingStatus
from .models import Admin
from django.contrib import messages


# Home Page View
def home(request):
    return render(request, 'home_page.html')



# Admin Panel View (Redirecting to Django's Admin Interface)
@login_required
def admin_panel(request):
    # return redirect('/admin/')
    pass






# Admin Panel View for Custom Admin Login
def admin_panel(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')

        try:
            # Validate credentials from the Admin table
            admin_user = Admin.objects.get(user_id=user_id, password=password)

            # If valid, redirect to the admin editing page
            request.session['admin_user_id'] = admin_user.user_id  # Set session for the logged-in admin
            return redirect('admin_editing')  # Redirect to the admin editing page
        except Admin.DoesNotExist:
            # If credentials are invalid, show error message
            messages.error(request, 'Invalid user ID or password.')
            return redirect('admin_panel')

    return render(request, 'admin_panel.html')  # Render the admin login page

# Admin Editing Page View (after successful login)
def admin_editing(request):
    # Ensure that the user is logged in as admin (session check)
    if 'admin_user_id' not in request.session:
        return redirect('admin_panel')  # If not logged in, redirect to admin login

    # Admin editing logic can be added here
    return render(request, 'admin_editing.html')

























# Vote Status View
@login_required
def vote_status(request):
    pass

# Voting View
@login_required
def vote(request):
    pass

# Result View
@login_required
def result(request):
    pass