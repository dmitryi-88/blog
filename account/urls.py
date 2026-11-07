from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('users/<str:username>/', views.public_profile, name='public_profile'),
]
