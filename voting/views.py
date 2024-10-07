from django.shortcuts import render

def index(request):
    candidates = [
        {'name': 'Candidate 1', 'image_url': 'images/candidate1.jpg'},
        {'name': 'Candidate 2', 'image_url': 'images/candidate2.jpg'},
        {'name': 'Candidate 3', 'image_url': 'images/candidate3.jpg'},
        {'name': 'Candidate 4', 'image_url': 'images/candidate4.jpg'},
        {'name': 'Candidate 5', 'image_url': 'images/candidate5.jpg'},
    ]
    return render(request, 'voting_main_page.html', {'candidates': candidates})






from django.shortcuts import render

def confirmation_view(request):
    context = {
        'voting_time': '10:00 AM',
        'voting_date': '2024-10-07',
        'voting_location': 'Delhi, India',
    }
    return render(request, 'after_successful_voting.html', context)
