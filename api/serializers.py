from taggit.models import Tag
from rest_framework import generics, serializers, filters

from posts.models import Post
from posts.serializers import PostSerializer


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = 'post_id'
