from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('add/', views.add_news, name='add_news'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='news/login.html'), name='login'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('category/<int:category_id>/', views.category_news, name='category_news'),
    path('news/<int:news_id>/edit/', views.edit_news, name='edit_news'),
    path('news/<int:news_id>/delete/', views.delete_news, name='delete_news'),
]
