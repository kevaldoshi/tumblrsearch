from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Blog
# Create your views here.

def index(request):
    blogs = Blog.objects.filter(tags__name__in=["keval"])
    return render_to_response('blogs/index.html', {'blogs': blogs})
