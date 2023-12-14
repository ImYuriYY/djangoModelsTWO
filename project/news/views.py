from django.shortcuts import render, redirect
from .forms import *
from .models import *

def index(request):
    newsPosts = Post.objects.all()
    return render(request, 'news/index.html', context={'newsPosts': newsPosts})


def createNews(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        urladdress = request.POST.get('urladdress')
        isPublic = request.POST.get('isPublic')
        if isPublic == 'on':
            isPublic = True
        else:
            isPublic = False
        category = request.POST.get('category')

        
        p, _ = Post.objects.get_or_create(
            title=title, 
            content=content, 
            urladdress=urladdress, 
            isPublic=isPublic, 
            category=category,
        )
        return redirect('home')
    else:
        form = CreatePost()
        return render(request, 'news/create.html', context={'form': form})



def change(request, id):
    try:
        post = Post.objects.get(pk=id)
        form = CreatePost()
        if request.method == 'POST':
            post.title = request.POST.get('title')
            post.content = request.POST.get('content')
            post.urladdress = request.POST.get('urladdress')
            post.isPublic = request.POST.get('isPublic')
            post.category = request.POST.get('category')

            post.save()
            return redirect('home')

        return render(request, 'news/change.html', context={'post': post, 'form': form})
    
    except:
        return redirect('create')
    




def delete(request, id):
    try:
        post = Post.objects.get(pk=id)
        post.delete()
        return redirect('home')
    except:
        return redirect('create')
    






