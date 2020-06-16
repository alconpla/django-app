from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('movie/<str:title>', views.movie_detail, name='movie_detail'),
    path('login', auth_views.LoginView.as_view(template_name='registration/login.html', redirect_authenticated_user=''), name='login'),
    path('', views.mylist, name='mylist'),
    path('showlist', views.showlist, name='showlist'),
    path('delete_from_list/<str:title>', views.delete_from_list, name='delete_from_list'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

]