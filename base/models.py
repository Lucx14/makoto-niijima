from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    body = models.TextField()
    published = models.BooleanField(default=True)
    likes = GenericRelation('Like', 'object_id', 'content_type_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likes.count()

    # def liked_by_current_user(self):
    #     return False


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, null=True, blank=True
    )
    content = models.CharField(max_length=200)
    likes = GenericRelation('Like', 'object_id', 'content_type_id')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def likes_count(self):
        return self.likes.count()

    # def liked_by_current_user(self):
    #     return False


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['object_id', 'content_type_id', 'user_id'], name='unique like')
        ]
