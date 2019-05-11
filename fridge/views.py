from django.shortcuts import render, redirect
from .forms import PostForm, UserForm, CopostForm
from .models import Post, Copost 
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime


# Create your views here.
def home(request):
    posts = Post.objects.all()
    food_list = request.POST.getlist('chk_info')
    foods = ''
    for food in food_list:
        foods = foods + food + '+'
    return render(request, 'home.html', {'posts':posts,'foods':foods,
    'food_list':food_list })


def new(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        post = form.save(commit=False)
        post.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'new.html', { 'form' : form })

def detail(request, post_pk):
    post = Post.objects.get(pk = post_pk)

    year = int(post.year)
    month = int(post.month)
    date = int(post.date)

    time_buy = datetime(year, month, date)
    time_now = datetime.now()

    exp_date = (time_buy - time_now).days
    return render(request, 'detail.html',{ 'post' : post, 'exp_date': exp_date })


def edit(request, post_pk):
    post = Post.objects.get(pk = post_pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'edit.html', {'form' : form })

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    post.delete()
    return redirect('home')

def about(request):
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
    post_list = []
    tag = str(Post.tag)
    co_contents = []
    for copost in coposts:
        post_list.append(copost.cocontents)
    
    return render(request, 'cohome.html', {'coposts' : coposts, 'post_list':post_list, 'tag':tag})


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
    copost = Copost.objects.get(pk = copost_pk)
    if request.method == "POST":
        form = CopostForm(request.POST, instance = copost)
        form.save()
        return redirect('codetail', copost.pk)
    else:
        form = CopostForm(instance = copost)
    return render(request, 'coedit.html', { 'form' : form })

def codelete(request, copost_pk):
    copost = Copost.objects.get(pk = copost_pk)
    copost.delete()
    return redirect('cohome')

    
def recipe(request):
    posts = Post.objects.all()
    food_list = request.POST.getlist('chk_info')
    foods = ''
    for food in food_list:
        foods = foods + food + '+'
    return render(request, 'recipe.html', {
        'posts':posts,
        'foods':foods,
        'food_list':food_list,
        'final_date':final_date
    })


def post_list(request):
    post_list = Post.objects.prefetch_related('tag_set').select_related('author__profile').all()
    return render(request, 'post/post_list.html', {'post_list':post_list,})