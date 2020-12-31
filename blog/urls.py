from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.createBlog, name='blog-create'),
    path('article/', views.viewBlog, name='blog-view'),
    path('my-blogs/', views.myBlogs, name='blog-personal'),
    path('settings/', views.profileSettings, name='setting'),
    path('cat/', views.special, name='special-cat')
]
