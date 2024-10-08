"""
URL configuration for voting_system_aurora project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from voting import views  # Import views from the voting app

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Voting page where candidates are displayed
    path('', views.voting_page, name='voting_page'),
    
    # Path for casting the vote
    path('voting/cast_vote/', views.cast_vote, name='cast_vote'),
    
    # Path for the confirmation page after successful voting
    path('voting/after_successful_voting/', views.after_successful_voting, name='after_successful_voting'),
]
