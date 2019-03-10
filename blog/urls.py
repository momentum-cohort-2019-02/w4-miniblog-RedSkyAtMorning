## This is catalog.urls

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('blog/blogs/', views.PostListView, name='postlist'),
    path('blog/blogger/<int:pk>', views.AboutBloggerView, name='aboutblogger''),
    path('blog/<int:pk', views.ThisPostView, name='thispost'),
    path('blog/bloggers/', views.BloggerListView, name='bloggerlist'),
    path('/blog/<int:pk>/create/', views.AddCommentsView, name='addcomment'),
]
