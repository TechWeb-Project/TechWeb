from django.db import models

# Create your models here.

# 이걸 어떻게 연결 시켜야지?!
class Tech(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    
    # 각각의 아티클 객체는 하나의 기술/기업 태그를 가지게 되므로 N:1 관계가 맞지 않나
    tech = models.ForeignKey(Tech, on_delete=models.CASCADE, related_name='article')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='article')
    # tech = models.ManyToManyField(Tech, related_name='article')
    # company = models.ManyToManyField(Company, related_name='article')

    title = models.CharField(max_length=100)
    content = models.TextField()

    # 혹시 몰라서 만들어준 업로드 날짜 필드
    # created_at = models.DateTimeField(auto_now_add=True)

    # url도 넣을 수 있지 않을까?
    # url = models.URLField()

    # 만약에 주제/기업에 따라 정해진 이미지를 고정적 넣어주면 굳이 모델에 할 필요가 없을 거 같아서 일단 주석 처리
    # thumbnail = models.ImageField()


