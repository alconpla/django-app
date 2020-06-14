from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<str:title>', views.movie_detail, name='movie_detail'),
    path('login', LoginView.as_view(), name='login'),
]