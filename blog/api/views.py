from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response

from blog.models import Post
from blog.api.serializers import PostSerializer


class PostCreateView(generics.CreateAPIView):

    serializer_class = PostSerializer

class PostListView(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateView(generics.RetrieveUpdateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDeleteView(generics.DestroyAPIView):

    queryset = Post.objects.all()

    def get(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)