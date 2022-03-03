from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Post
from .forms import PostForm

def index(request):
  response = { "title": 'Blogs', "blogs": Post.objects.all() }
  return render(request, 'index.html', response)

def new_post(request):
  form = PostForm(request.POST or None)
  if form.is_valid():
    Post.objects.create(**form.cleaned_data)
    messages.add_message(request, messages.SUCCESS, "Post created successfully.")
    return redirect('/')
  else:
    return render(request, 'new_post.html', { "title": 'New post', "form": form })

def update_post(request, id):
  post = Post.objects.get(id = id)
  if request.POST:
    form = PostForm(request.POST or None, instance = post)
    if form.is_valid():
      form.save()
      return redirect('/')
  else:
    form = PostForm(request.GET or None, instance = post)
    return render(request, 'update_post.html', { "title": 'Update post', "form": form, "post": post})

def view_post(request, id):
  post = Post.objects.get(id = id)
  return render(request, 'post.html', { "title": "{post.title}", "post": post })

# def destroy_post(request, id):
#   if request.DELETE:
#     post = Post.objects.get(id = id)
#     post.delete()
#     messages.add_message(request, messages.SUCCESS, "Post destroy successfully.")
#     return redirect('/')
