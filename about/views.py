from django.template.response import TemplateResponse

# Create your views here.
def index(request):
    args = {}
    args['app_url'] = 'about'
    args['title'] = 'About Page'
    return TemplateResponse(request, 'about/about.html', args)
