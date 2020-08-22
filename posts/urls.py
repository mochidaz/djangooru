from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.views import PostView, DetailView, TagView, IndexView, upload_view

urlpatterns = [
    path('', PostView.as_view(), name="posts"),
    path('upload', upload_view, name='upload'),
    path('<post_id>', DetailView, name="post_detail"),
]
