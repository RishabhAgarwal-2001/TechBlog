from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import redirect
from .forms import AuthorForm
from .models import Post
from register.models import Users
import datetime
# Create your views here.
def viewBlog(request):
    args = {}
    if request.method=='GET':
        id = request.GET["Id"]
        p = Post.objects.filter(id=id)[0]
        args["article"] = p
        return TemplateResponse(request, "blog/article.html", args)
    return redirect('home-index')
def createBlog(request):
    if request.method=='POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            u = Users.objects.filter(username=request.session["user"])[0]
            p = Post.objects.create(title=form.cleaned_data['title'],
                                    username=u, content=form.cleaned_data['content'],
                                    pub_date=datetime.datetime.now,
                                    category=form.cleaned_data['category'])
            p.save()
            return redirect('home-index')
    else:
        form = AuthorForm()
    return TemplateResponse(request, 'blog/new.html', {'form': form})

def myBlogs(request):
    if request.session["user"]:
        u = Users.objects.filter(username=request.session["user"])[0]
        p = Post.objects.filter(username=u)
        return TemplateResponse(request, 'blog/myBlogs.html', {'posts':p})
    return redirect('home-index')

def profileSettings(request):
    args = {}
    if request.session["user"]:
        u = Users.objects.filter(username=request.session["user"])[0]
        args["user"] = u
        return TemplateResponse(request, 'blog/profileSetting.html', args)
    return redirect('home-index')

def special(request):
    args = {}
    if(request.method=='GET'):
        p = Post.objects.filter(category=request.GET["C"])
        args["posts"] = p
        return TemplateResponse(request, 'home/index.html', args)
    return redirect('home/index.html')
