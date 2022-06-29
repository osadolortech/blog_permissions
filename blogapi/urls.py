from django import views
from django.urls import path
from .views import BlogList, BlogDetail,RegisterUserApi,UserDetailAPI

urlpatterns = [
    path('<int:pk>', BlogDetail.as_view(), name='BlogView'),
    path('', BlogList.as_view(), name='BlogPost'),
    path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserApi.as_view()),
    
]