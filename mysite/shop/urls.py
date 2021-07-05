from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('news/', views.news, name="news"),
    path('team/', views.team, name="team"),
    path('course/', views.course, name="course"),
    path('video/<int:pk>/<int:pks>/', views.video, name="video"),
]
