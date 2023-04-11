from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blogApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about-us/', views.about_view, name='about-us'),
    path('createpost/', views.create_newpost, name='createpost'),
    #path('create-post/', views.create_newpost, name="create-post")
]