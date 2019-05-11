from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Post 

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
