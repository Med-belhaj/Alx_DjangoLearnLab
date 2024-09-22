from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser
from .serializers import UserSerializer, RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if user_to_follow == request.user:
        return Response({'detail': "You can't follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)
    return Response({'detail': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

    if user_to_unfollow == request.user:
        return Response({'detail': "You can't unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({'detail': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)

