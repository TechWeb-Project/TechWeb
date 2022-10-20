from django.db import models
from django.conf import settings
from . import articles


# 유저들이 쓸 수 있는 게시글
class UserArticle(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # nickname = user.nickname 하면 되나? 어차피 같은 테이블 참조
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200)
    created_now = models.DateTimeField(auto_now_add=True)
    updated_now = models.DateTimeFiedl(auto_now=True)
    tech = models.ManyToManyField(articles.Tech)
    company = models.ManyToManyField(articles.Company)

# 유저들의 게시글에 다는 댓글
class Comment(models.Model):
    user_article = models.ForeignKey(UserArticle, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)
    created_now = models.DateTimeField(auto_now_add=True)
    updated_now = models.DateTimeFiedl(auto_now=True)