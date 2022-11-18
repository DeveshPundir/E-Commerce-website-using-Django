from django.shortcuts import render
from .models import blogpost
def index(request):
    myposts=blogpost.objects.all()
    
    return render(request,'blog/index.html',{'myposts':myposts})
def Blogpost(request,id):
    post=blogpost.objects.filter(post_id=id)[0]
    return render(request,'blog/blogPost.html',{'post':post})
# Create your views here.
