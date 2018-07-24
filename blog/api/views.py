import sys

from django.http import HttpResponse

from rest_framework import generics
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from blog.models import Post, Comment
from blog.api.serializers import PostSerializer, CommentSerializer

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

class PostCommentCreateView(generics.CreateAPIView):

    serializer_class = CommentSerializer

    def create(self, request, *args, **kwargs):

        data = JSONParser().parse(request)
        try:
            post = Post.objects.get(id=kwargs['pk'])
            serializer = CommentSerializer(data=data)
            if serializer.is_valid():
                comment = serializer.save()
                post.comment_set.add(comment)
                return Response(post)
        except Comment.DoesNotExist:
            return HttpResponse(status=404)