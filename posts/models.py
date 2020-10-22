from django.db import models
from django.contrib.auth.models import User

from django_userforeignkey.models.fields import UserForeignKey
from taggit.managers import TaggableManager


class Post(models.Model):
    uploader = UserForeignKey(auto_user_add=True)
    artist = models.CharField(default="", max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    source = models.URLField(blank=True, default="")
    image = models.ImageField(upload_to='img')
    tags = TaggableManager()
    post_id = models.AutoField(primary_key=True, unique=True)

    class Meta:
        ordering = ['-published']

    def __str__(self):
        return f"Post #{self.post_id}"


#class Favorite(models.Model):
#    user = models.OneToOneField(User, on_delete=models.CASCADE)
#    favorite = models.ManyToManyField(Post)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = UserForeignKey(auto_user_add=True)
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'Comment {self.comment} by {self.name}'
    
