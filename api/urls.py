from django.urls import path, include, re_path


from posts import views
from posts.serializers import router
from .serializers import PostListView

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', PostListView.as_view()),
    #re_path('^posts/', PostListView.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]

