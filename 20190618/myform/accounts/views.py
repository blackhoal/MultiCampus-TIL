from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .forms import UserCustomChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def signup(request):
    if request.user.is_authenticated: # 190618
        return redirect('boards:index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 190618 해당 아이디로 로그인한 채로 바로 index 페이지로 이동
            return redirect('boards:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.user.is_authenticated: # 190618
        return redirect('boards:index')
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('boards:index')
    else:
        form = AuthenticationForm()
    context ={'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request): # Session을 Delete하는 방식으로 로그아웃 기능 구현
    if request.method == 'POST':
        auth_logout(request)
        return redirect('boards:index')
    else:
        return redirect('boards:index')

def delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('boards:index')
    else:
        return redirect('boards:index')

def edit(request):
    if request.method == 'POST':
        form = UserCustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('boards:index')
    else:
        form = UserCustomChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'accounts/edit.html', context)
