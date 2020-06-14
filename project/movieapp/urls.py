from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<str:title>', views.movie_detail, name='movie_detail'),
    path('login', auth_views.LoginView.as_view(), name='login'),
]