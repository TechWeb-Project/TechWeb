from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(
        label='닉네임',
        max_length=15,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                'autofocus': True
            }
        )
    )

    username = forms.CharField(
        label='아이디',
        max_length=30,
        help_text='',
        widget=forms.TextInput(
            attrs={
            }
        )
    )

    email = forms.EmailField(
        label='이메일',
        max_length=50,
        widget=forms.TextInput(
            attrs={
            }
        )
    )

    password1 = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput(
            attrs={
            }
        )
    )

    password2 = forms.CharField(
        label='비밀번호 확인',
        help_text='',
        widget=forms.PasswordInput(
            attrs={
                }
        )
    )

    class Meta:
        model = get_user_model()
        fields = ('nickname', 'username', 'email', 'password1', 'password2',)


class CustomUserChangeForm(UserChangeForm):

    nickname = forms.CharField(
        label='닉네임',
        max_length=15,
        min_length=1,
        widget=forms.TextInput(
            attrs={
                'autofocus': True
            }
        )
    )

    email = forms.EmailField(
        label='이메일',
        max_length=50,
        widget=forms.TextInput(
            attrs={
            }
        )
    )


    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('nickname', 'email',)
