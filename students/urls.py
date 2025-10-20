from django.urls import path
from . import views

urlpatterns = [
    path('clubs/', views.clubs_list, name='clubs_list'),
    path('clubs/add/', views.add_club, name='add_club'),
    path('clubs/<int:club_id>/', views.club_detail, name='club_detail'),
    path('clubs/<int:club_id>/edit/', views.edit_club, name='edit_club'),
    path('clubs/<int:club_id>/delete/', views.delete_club, name='delete_club'),
]


