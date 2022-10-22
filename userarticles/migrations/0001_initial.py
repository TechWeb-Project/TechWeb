# Generated by Django 3.2.9 on 2022-10-21 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(max_length=200)),
                ('created_now', models.DateTimeField(auto_now_add=True)),
                ('updated_now', models.DateTimeField(auto_now=True)),
                ('company', models.ManyToManyField(to='articles.Company')),
                ('tech', models.ManyToManyField(to='articles.Tech')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_like', models.ManyToManyField(related_name='like_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=200)),
                ('created_now', models.DateTimeField(auto_now_add=True)),
                ('updated_now', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userarticles.userarticle')),
            ],
        ),
    ]
