from django.urls import path
from .views import BlogList, BlogDetail,RegisterUserApi,UserDetailAPI,Login,Logout
urlpatterns = [
    path('<int:pk>', BlogDetail.as_view(), name='BlogView'),
    path('', BlogList.as_view(), name='BlogPost'),
    path("get-details",UserDetailAPI.as_view()),
    path('register',RegisterUserApi.as_view()),
    path('login',Login.as_view()),
    path('logout', Logout.as_view())   
]