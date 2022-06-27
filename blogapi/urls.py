from django import views
from django.urls import path
from .views import BlogList, BlogDetail

urlpatterns = [
    path('<int:pk>', BlogDetail.as_view(), name='BlogView'),
    path('', BlogList.as_view(), name='BlogPost'),
    
]