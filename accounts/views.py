from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from IPython import embed

from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            user = new_user.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        new_user = UserCreationForm()
    context = {
        'new_user': new_user
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('articles:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST) # modelform이 아니다
        if form.is_valid():
            # embed()
            # 로그인
            user = form.get_user()
            auth_login(request, user)
            return redirect(request.GET.get('next') or 'articles:index') # 로그인을 하지 않은 상태에서 접근하면 'next'가 None (단축평가)
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:info')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def info(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'accounts/info.html', context)

@login_required
def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user) # 반드시 첫번째 인자로 user
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)