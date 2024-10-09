from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from user_management.models import Candidate, CitizenData
from aadhaar_voter_card.models import AadhaarVerification
from voting.models import VotingStatus
from .models import Admin
from django.contrib import messages
from .models import CitizenData


# Home Page View
def home(request):
    return render(request, 'home_page.html')


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


@login_required
def admin_editing(request):
    # Ensure the admin user is logged in (session check)
    if 'admin_user_id' not in request.session:
        return redirect('admin_panel')

    # Render the admin editing page with buttons
    return render(request, 'admin_editing.html')



@login_required
def add_new_citizen(request):
    if request.method == 'POST':
        # Extract data from POST request
        citizen_name = request.POST.get('citizen_name')
        father_name = request.POST.get('father_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        address = request.POST.get('address')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        aadhaar_number = request.POST.get('aadhaar_number')
        voter_id_number = request.POST.get('voter_id_number')
        photo_aadhaar = request.FILES.get('photo_aadhaar')
        photo_voter = request.FILES.get('photo_voter')

        # Create a new CitizenData object and save it to the database
        try:
            citizen = CitizenData.objects.create(
                citizen_name=citizen_name,
                father_name=father_name,
                gender=gender,
                dob=dob,
                address=address,
                mobile=mobile,
                email=email,
                aadhaar_number=aadhaar_number,
                voter_id_number=voter_id_number,
                photo_aadhaar=photo_aadhaar,
                photo_voter=photo_voter
            )
            citizen.save()
            
            # Show a success message and redirect to the admin editing page
            messages.success(request, 'Citizen successfully registered!')
            return redirect('admin_editing')
        except Exception as e:
            # Show an error message if the registration fails
            messages.error(request, f'Error: {str(e)}')
    
    return render(request, 'add_new_citizen.html')












@login_required
def edit_existing_citizen(request):
    return redirect('edit_existing_citizen')  # You can replace this with the actual logic

@login_required
def add_edit_candidate(request):
    return redirect('add_edit_candidate')  # You can replace this with the actual logic
























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