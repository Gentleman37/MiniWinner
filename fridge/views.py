from django.shortcuts import render, redirect
from .forms import PostForm, UserForm
from .models import Post 
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'new.html', { 'form' : form })



def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            auth.login(request, new_user)
            return redirect('')
        else:
            form = UserForm()
            error = "아이디가 이미 존재합니다."
            return render(request, 'registration/signup.html', {'form': form, 'error': error} )
    else:
        form = UserForm()
        return render(request, 'registration/signup.html', {'form': form} )
