from django.shortcuts import render
from rest_framework import generics
from rest_framework.compat import get_regex_pattern
from .serializers import PostSerializer
from .models import Post
from .permissions import IsAuthororReadonly

# Create your views here.

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthororReadonly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    


