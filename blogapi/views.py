
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import BlogModel
from .serializations import BlogSerializers,RegisterSerilizer,UserSerializer
from rest_framework import filters
from rest_framework.permissions import BasePermission,AllowAny,SAFE_METHODS, IsAuthenticatedOrReadOnly


class UserDetailAPI(APIView):
    permission_classes = [AllowAny]
    def get(self, request,*args,**kwargs):
        user = User.objects.get(author=request.user.id)
        serializer= UserSerializer(user)
        return Response(serializer.data)

class RegisterUserApi(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class =RegisterSerilizer

class BlogUserwritePermissions(BasePermission):
    message = "Editing post is retricted to to the author only"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class BlogList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['=title', '^title']

class BlogDetail(generics.RetrieveUpdateDestroyAPIView, BlogUserwritePermissions):
    permission_classes = [BlogUserwritePermissions]
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['=title', '^title']
