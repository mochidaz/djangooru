from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from posts.views import PostView, DetailView, TagView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostView, name="index"),
    path('accounts/', include('accounts.urls')),
    path('post/<post_id>', DetailView, name="post_detail"),
    path('tags/<tags>', TagView, name='tag_detail')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
