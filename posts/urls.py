from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.views import PostView, DetailView, TagView, IndexView

urlpatterns = [
    path('', PostView.as_view(), name="posts"),
    path('<post_id>', DetailView, name="post_detail"),

]