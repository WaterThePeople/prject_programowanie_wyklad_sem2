from django.shortcuts import render
from .models import Post

posts = [
    {
        'author':'MAX',
        'title':'Blog Post 1',
        'content':'First post',
        'date_posted':'11 May 2020'
    },
    {
        'author':'MEKS',
        'title':'Blog Post 2',
        'content':'Second post',
        'date_posted':'26 June 2021'
    }
]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'home_page/home.html',context)

def welcome(request):
    return render(request,'home_page/welcome.html',{'title':'Welcome'})