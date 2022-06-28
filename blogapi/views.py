
from rest_framework import generics
from .models import BlogModel
from .serializations import BlogSerializers
from rest_framework.permissions import BasePermission, DjangoModelPermissionsOrAnonReadOnly,SAFE_METHODS

class BlogUserwritePermissions(BasePermission):
    message = "Editing post is retricted to to the author only"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class BlogList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers

class BlogDetail(generics.RetrieveUpdateDestroyAPIView, BlogUserwritePermissions):
    permission_classes = [BlogUserwritePermissions]
    queryset = BlogModel.objects.all()
    serializer_class = BlogSerializers
