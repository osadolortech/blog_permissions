from dataclasses import fields
from rest_framework import serializers
from .models import BlogModel


class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = (
            'id','author','title','content'
        )
