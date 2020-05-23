from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.

def index(request):
    return HttpResponse('Hello!, world blog')


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'
