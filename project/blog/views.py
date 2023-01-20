from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from .models import * 
from .forms import *
# Create your views here.

def index(request):
    blogs = Blog.objects.all()

    paginator = Paginator(blogs , 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'pages/index.html', {'blogs':page_obj})


def about(request):
    return render(request, 'pages/about.html', {'name':'Mohammed'})


def detail(request , id):
    blog = Blog.objects.get(id = id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.blog = blog
            myform.owner = request.user
            myform.save()
    return render(request, 'pages/detail.html', {'blog':blog , 'comments' : blog.comments.all, 'form' : CommentForm()})



def N_post(request):
    if request.method == 'POST':
        add_blog = BlogForm(request.POST , request.FILES)

        if add_blog.is_valid():
            myform = add_blog.save(commit=False)
            myform.owner = request.user
            myform.save()

            return redirect('/')

    return render(request, 'pages/new_post.html', {'form':BlogForm(),})


def D_post(request , id):
    blog = get_object_or_404(Blog , id = id)

    if request.method == 'POST':
        blog.delete()
        return redirect('/')

    return render(request, 'pages/post_confirm_delete.html', {'blog':blog})


def U_post(request , id):
    blog_id = Blog.objects.get(id = id)

    if request.method == 'POST':
        blog_save = BlogForm(request.POST , request.FILES , instance = blog_id)

        if blog_save.is_valid():
            blog_save.save()
            return redirect('/')
    else:
        blog_save = BlogForm(instance = blog_id)

    context = {
        'form': blog_save,
    }
    return render(request, 'pages/post_update.html', context)