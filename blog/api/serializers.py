import sys

from rest_framework import serializers

from blog.models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'content',
            'timestamp'
        ]

    def validate_title(self, value):
        queryset = Post.objects.filter(title=value)
        if queryset.exists():
            raise serializers.ValidationError("This title is already been used")
        return value


