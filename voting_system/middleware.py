# your_app/middleware.py

from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Define paths that should NOT require custom admin login
        allowed_paths = [
            reverse('home'),  # Home page
            reverse('admin_panel'),  # Custom admin login page
            reverse('logout'),  # Logout
            '/admin/',  # Django superuser login and paths
            reverse('vote_status'),  # Public paths that don't need admin login
            reverse('result'),
            reverse('vote')
        ]

        # Allow Django's superuser login or other non-admin routes
        if request.path.startswith('/admin/') or request.path in allowed_paths:
            return self.get_response(request)

        # If not logged in as custom admin and trying to access restricted admin pages, redirect to custom admin login
        if 'admin_user_id' not in request.session and 'admin_panel' not in request.path:
            return redirect('admin_panel')  # Redirect to custom admin login

        return self.get_response(request)
