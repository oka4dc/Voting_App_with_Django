from django.urls import path
from PollsApp import views


urlpatterns = [
    path('', views.index, name='index'),
]