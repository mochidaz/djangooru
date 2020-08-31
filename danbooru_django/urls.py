from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.views import TagView, IndexView
from posts.serializers import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name="index"),
    path('api/', include("api.urls")),
    path('api-auth/', include('rest_framework.urls', namespace="rest_framework")),
    path('posts/', include('posts.urls')),
    path('users/', include('accounts.urls')),
    #path('tags/', TagList, name="taglist"),
    path('tags/<tags>', TagView, name='tag_detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
