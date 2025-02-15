from . import views
from django.urls import path
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('sign-up', views.sign_up, name='signup'),
    path('create-post', views.create_post, name='create_post'),
    path('logout/', views.LogOut, name='logout')
]
