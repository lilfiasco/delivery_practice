from django.urls import path
from .views import (
    UserRegisrtrationView,
    CustomLoginView,
    CustomLogoutView,
    ProfileDetailView,
    ProfileUpdateView,
    CustomUserPasswordChange,
    CoworkerRegisrtrationView,

)


urlpatterns = [
    path('registration/', UserRegisrtrationView.as_view(template_name='auths/registration.html'),name="registration"),
    path('registration_coworker/', CoworkerRegisrtrationView.as_view(template_name='auths/registration_coworker.html'),name="registration_coworker"),
    path('login/',CustomLoginView.as_view(),name='login'),
    path('logout/',CustomLogoutView.as_view(),name='logout'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('update_profile/<int:pk>/', ProfileUpdateView.as_view(), name='update_profile'),
    path('change_password/', CustomUserPasswordChange.as_view(),name='change_password'),

]
