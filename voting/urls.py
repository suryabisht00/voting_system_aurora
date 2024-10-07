# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('candidates/', views.view_candidates, name='view_candidates'),
    path('vote/<int:candidate_id>/', views.cast_vote, name='cast_vote'),
    path('my_vote/', views.view_vote, name='view_vote'),
]
