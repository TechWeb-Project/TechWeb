from xml.etree.ElementTree import Comment
from django import forms
from .models import UserArticle


class UserArticleForm(forms.ModelForm):

    class Meta:
        model = UserArticle
        exclude = ('user', 'user_like',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('user_article', 'user',)