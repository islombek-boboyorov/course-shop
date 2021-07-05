from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard_page, name="dashboard"),
    path('login/', views.dashboard_login, name="login"),
    path('logout/', views.dashboard_logout, name="logout"),

    path('item/', views.item_list, name="item_list"),
    path('item/add/', views.item_create, name="item_add"),
    path('item/<int:pk>/edit/', views.item_edit, name="item_edit"),
    path('item/<int:pk>/delete/', views.item_delete, name="item_delete"),

    path('course/', views.course_list, name="course_list"),
    path('course/add/', views.course_create, name="course_add"),
    path('course/<int:pk>/edit/', views.course_edit, name="course_edit"),
    path('course/<int:pk>/delete/', views.course_delete, name="course_delete"),

    path('about/', views.about_list, name="about_list"),
    path('about/add/', views.about_create, name="about_add"),
    path('about/<int:pk>/edit/', views.about_edit, name="about_edit"),
    path('about/<int:pk>/delete/', views.about_delete, name="about_delete"),

    path('news/', views.news_list, name="news_list"),
    path('news/add/', views.news_create, name="new_add"),
    path('news/<int:pk>/edit/', views.news_edit, name="new_edit"),
    path('news/<int:pk>/delete/', views.news_delete, name="new_delete"),

    path('video/', views.video_list, name="video_list"),
    path('video/add/', views.video_create, name="video_add"),
    path('video/<int:pk>/edit/', views.video_edit, name="video_edit"),
    path('video/<int:pk>/delete/', views.video_delete, name="video_delete"),
]
