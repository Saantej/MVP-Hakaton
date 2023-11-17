from django.urls import path

from user.views import login, register, logout, profile

app_name = 'user'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]
