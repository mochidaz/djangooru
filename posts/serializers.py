from rest_framework import serializers, viewsets, routers

from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
