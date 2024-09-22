from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import filters

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']  # Enable searching by title and content

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # Retrieve users that the current user is following
        following_users = user.following.all()
        # Filter posts by those authored by following users, ordered by creation date
        return Post.objects.filter(author__in=following_users).order_by('-created_at')


from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.shortcuts import get_object_or_404  # Import get_object_or_404 here
from .models import Post, Like
from notifications.models import Notification  # Assuming you have a Notification model

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    # Use get_object_or_404 to retrieve the post safely, or return a 404 error if not found
    post = generics.get_object_or_404(Post, pk=pk)

    # Create a like object if it doesn't already exist
    like, created = Like.objects.get_or_create(user=request.user, post=post)

    if not created:
        return Response({'detail': 'You have already liked this post.'}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create a notification for the post author if the post is liked
    Notification.objects.create(
        recipient=post.author,
        actor=request.user,
        verb='liked your post',
        target=post
    )
    
    return Response({'detail': 'Post liked and notification sent.'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    # Use get_object_or_404 to retrieve the post safely, or return a 404 error if not found
    post = get_object_or_404(Post, pk=pk)

    # Try to get the like object and delete it if it exists
    like = Like.objects.filter(user=request.user, post=post).first()
    if like:
        like.delete()
        return Response({'detail': 'Post unliked.'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

        like.delete()
        return Response({'detail': 'Post unliked.'}, status=status.HTTP_204_NO_CONTENT)
    
    return Response({'detail': 'You have not liked this post.'}, status=status.HTTP_400_BAD_REQUEST)

#generics.get_object_or_404(Post, pk=pk)
