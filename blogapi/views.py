from rest_framework import generics
from .models import BlogModel
from .serializations import BlogSerializers


class BlogList(generics.ListCreateAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
