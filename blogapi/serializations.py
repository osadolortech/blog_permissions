from rest_framework import serializers
from .models import BlogModel


class BlogSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = BlogModel
        fields = (
            'id','author','title','content','published_at'
        )
