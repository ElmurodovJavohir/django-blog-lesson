from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=256)


class Post(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    content = models.TextField()

    category = models.ManyToManyField(Category)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    text = models.TextField()

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
