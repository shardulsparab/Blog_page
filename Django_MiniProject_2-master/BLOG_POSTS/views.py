from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from . import forms
from . import form1
from.models import login
from.models import createblog

# Create your views here.

def home(request):
    return HttpResponse("Hello I am in home")


def create(request):
    if request.method=="POST":
        form=forms.loginform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form=forms.loginform()


    return render(request,'BLOG_POSTS/signup.html',{'form':form})


def success(request):
    return render(request,'BLOG_POSTS/success.html')


def create_blog(request):
    if request.method=="POST":
        form=form1.create_blog(request.POST,request.FILES)
        if form.is_valid():
            # form = createblog.objects.get(id=id)
            form.save()
            return redirect("success")


    else:
        form=form1.create_blog()
    return render(request,'BLOG_POSTS/POST_FORM.html',{'form':form})



def show(request):
    create_blogs=createblog.objects.all()
    return render(request,'BLOG_POSTS/POST_LIST.HTML',{'create_blogs':create_blogs})

def destroy(request,id):
    create_blogs = createblog.objects.get(id=id)
    create_blogs.delete()
    return redirect("show")

def edit(request,id):
    createblogs=createblog.objects.get(id=id)
    return render(request,"BLOG_POSTS/eedit.html",{'createblogs':createblogs})

def update(request,id):
    createblogs=createblog.objects.get(id=id)
    form=form1.create_blog(request.POST,instance=createblogs)
    if form.is_valid():
        form.save()
        return redirect("show")
    return render(request,"BLOG_POSTS/eedit.html",{'createblogs':createblogs})

class homepageview(TemplateView):
    template_name='BLOG_POSTS/firstpage.html'


def test(request):
    return render(request,"BLOG_POSTS/test.html")