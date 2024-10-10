"""
URL configuration for voting_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from user_management import views
from user_management.views import logout_view 

from user_management.views import (
    admin_panel,
    admin_editing,
    add_new_citizen,
    edit_existing_citizen,
    citizen_search_ajax,
    update_citizen,
    edit_citizen2,
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('admin_panel/', admin_panel, name='admin_panel'),
    path('admin_editing/', admin_editing, name='admin_editing'),
    path('add_new_citizen/', add_new_citizen, name='add_new_citizen'),
    path('logout/', logout_view, name='logout'), 
    path('edit_existing_citizen/', edit_existing_citizen, name='edit_existing_citizen'),
    path('add_edit_candidate/', views.add_edit_candidate, name='add_edit_candidate'),
    path('citizen_search_ajax/', citizen_search_ajax, name='citizen_search_ajax'),
    path('edit_citizen/<int:citizen_id>/', edit_citizen2, name='edit_citizen2'),
    path('update_citizen/<int:citizen_id>/', update_citizen, name='update_citizen'),
    path('vote_status/', views.vote_status, name='vote_status'),
    path('vote/', views.vote, name='vote'),
    path('result/', views.result, name='result'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
