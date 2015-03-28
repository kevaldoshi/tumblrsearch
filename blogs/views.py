from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Blog
import utils
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login
# Create your views here.

def index(request):
    return render_to_response('blogs/index.html', context_instance=RequestContext(request))
    
    
def search(request):
    template = 'blogs/list.html'
    keyword = request.POST['keyword']
    blogs = Blog.objects.filter(tags__name__in=[keyword])
    if len(blogs) == 0:
        tumblr = utils.TumblrClient()
        tumblr.fetch(keyword)
        blogs = Blog.objects.filter(tags__name__in=[keyword])
    return render_to_response(template, {'blogs': blogs})   
