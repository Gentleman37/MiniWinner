from django.shortcuts import render, redirect
from .forms import PostForm, UserForm, CopostForm
from .models import Post, Copost 
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request, 'home.html')

def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        post = form.save(commit=False)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'new.html', { 'form' : form })

def detail(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    return render(request, 'detail.html',{ 'post' : post })

def edit(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance = post)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm( instance = post )
    return render(request, 'edit.html', {'form' : form })

def delete(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    post.delete()
    return redirect('home')

def about(request)
    return render(request, 'about.html')
    
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


def cohome(request):
    coposts = Copost.objects.all()
    return render(request, 'cohome,html', {'coposts' : coposts})


def conew(request):
    if request.method == 'POST':
        form = CopostForm(request.POST)
        copost = form.save(commit=False)
        form.save()
        return redirect('codetail', copost.pk)
    else:
        form = CopostForm()
        return render(request,'conew.html', { 'form' : form })

def codetail(request, copost_pk):
    copost = Copost.objects.get(pk=copost_pk)
    return render(request,'codetail.html', { 'copost' : copost })

def coedit(request, copost_pk):
    copost = Copost.objests.get(pk = copost_pk)
    if request.method == "POST":
        form = Copostform(request.POST, instance = copost)
        form.save()
        return redirect('codetail', copost.pk)
    else:
        form = CopostForm(instance = copost)
    return render(request, 'coedit.html', { 'form' : form })

def codelete(request, copost_pk):
    copost = Copost.objects.get(pk = copost_pk)
    copost.codelete()
    return redirect('cohome')

    
def recipe(request):
    posts = Post.objects.all()
    food_list = request.POST.getlist('chk_info')
    return render(request, 'recipe.html', {
        'posts':posts,
        'food_list':food_list
    })
