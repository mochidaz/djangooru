from rest_framework import serializers, viewsets, routers
from taggit_serializer.serializers import TaggitSerializer, TagListSerializerField

from .models import Post

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    
    image = serializers.ImageField(max_length=None, use_url=True, required=True)
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
