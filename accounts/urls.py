from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts import views
from accounts.views import UserRegistrationView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('profile/', views.profile_information_view, name='profile')
]