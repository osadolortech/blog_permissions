
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import BlogModel
from .serializations import BlogSerializers,RegisterSerilizer,UserSerializer
from rest_framework import filters
from rest_framework.permissions import BasePermission,AllowAny,SAFE_METHODS, IsAuthenticatedOrReadOnly


class UserDetailAPI(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class RegisterUserApi(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class =RegisterSerilizer

class BlogUserwritePermissions(BasePermission):
    message = "Editing post is retricted to to the author only"
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user

class BlogList(generics.ListCreateAPIView,BlogUserwritePermissions):
    permission_classes = [IsAuthenticatedOrReadOnly,BlogUserwritePermissions]
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


class Login(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    
    def post(self,request):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error":"please fill all filds"}, status=status.HTTP_400_BAD_REQUEST)
        check_user = User.objects.filter(username=username).exists()
        if check_user == False:
            return Response({"error":"username does not exists"},status=status.HTTP_404_NOT_FOUND)
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=request.user)
            data = {
                "token": token.key,
                "user_id":request.user.pk,
                "username": request.user.username
            }
            return Response({"sucess":"sucessful login","data": data}, status=status.HTTP_200_OK)
        else:
            return Response({"error":"error details login"}, status=status.HTTP_400_BAD_REQUEST)


class Logout(APIView):
    permission_classes= [AllowAny]
    def get(self,request):
        logout(request)
        return Response("sucessfully logout")



