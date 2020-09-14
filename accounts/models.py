from django.db import models
from django.contrib.auth.models import User

from posts.models import Post


class User(User):
    favorite = models.ManyToManyField(Post)
