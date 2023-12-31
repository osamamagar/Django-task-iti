from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
# from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from posts.forms import  PostModelForm
from posts.models import Post

# Create your views here.


class PostsList(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'

class PostDetails(DetailView):
    model = Post
    template_name = 'posts/show.html'

class PostUpdate(UpdateView):
    model = Post
    template_name = 'posts/edit.html'
    form_class = PostModelForm
    success_url = reverse_lazy('posts.list')


class PostCreate(CreateView):
    model = Post
    template_name = 'posts/create.html'
    form_class = PostModelForm
    success_url = reverse_lazy('posts.list')



class PostDelete(DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('posts.list')    