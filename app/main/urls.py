from django.urls import path

from main.views import index, hakatons, about_hackathon, about

app_name = 'main'


urlpatterns = [
    path('', index, name='index'),
    path('hakatons/', hakatons, name='hakatons'),
    path('about_hackathon/', about_hackathon, name='about_hackathon'),
    path('about/', about, name='about'),

]