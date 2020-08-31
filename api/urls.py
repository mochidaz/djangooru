from django.urls import path, include


from posts import views
from posts.serializers import router

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]

