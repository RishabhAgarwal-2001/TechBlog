from django.template.response import TemplateResponse
from blog.models import Post
# Create your views here.
def index(request):
    args = {}
    if(request.session.get('login_message')):
        if(request.session['login_message']=="S"):
            args['login'] = 'S'
        if(request.session['login_message']=="F"):
            args['login'] = 'F'
        request.session['login_message'] = ""
    args['app_url'] = 'home'
    args['title'] = 'Home Page'
    allPosts = Post.objects.all()
    args['posts'] = allPosts
    if(request.method=='POST'):
        print("LOGIN REQUEST GENERATED")
        print(request.POST["uName"])
        print(request.POST["pwd"])
    return TemplateResponse(request, 'home/index.html', args)
