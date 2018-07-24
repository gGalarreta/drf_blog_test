import sys

from rest_framework import serializers

from blog.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model  = Comment
        fields = [
            'id',
            'commenter',
            'body'
        ]

class PostSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model  = Post
        fields = [
            'id',
            'title',
            'content',
            'comments',
            'timestamp'
        ]
        depth = 1

    def validate_title(self, value):
        queryset = Post.objects.filter(title=value)
        if queryset.exists():
            raise serializers.ValidationError("This title is already been used")
        return value

