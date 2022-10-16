from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.

@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        # (수정: 메인페이지로 보내야됨)
        return redirect('accounts:login')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'accounts:login') # (수정: 메인페이지로 보내야됨)
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)


@require_POST
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    # (수정: 메인페이지로 보내야됨)
    return redirect('accounts:login')


@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        # (수정: 메인페이지로 보내야됨)
        return redirect('accounts:login')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            # (수정: 메인페이지로 보내야됨)
            return redirect('accounts:login')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)


@require_POST
def delete(request):
    if request.user.is_authenticated:
        request.user.delete()
        auth_logout(request)
    # (수정: 메인페이지로 보내야됨)
    return redirect('accounts:login')


@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # (수정: 메인페이지로 보내야됨)
            return redirect('accounts:login')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)



@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            # (수정: 메인페이지로 보내야됨)
            return redirect('accounts:login')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)