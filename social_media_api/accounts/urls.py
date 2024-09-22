from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import RegisterView, ProfileView
from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),  # User registration
    path('login/', obtain_auth_token, name='login'),  # User login to obtain token
    path('profile/', ProfileView.as_view(), name='profile'),  # User profile management
    path('follow/<int:user_id>/', follow_user, name='follow_user'),
    path('unfollow/<int:user_id>/', unfollow_user, name='unfollow_user'),
]
