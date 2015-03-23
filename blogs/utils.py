from django.core.exceptions import ImproperlyConfigured
from .models import Blog
import pytumblr
import json
import dateutil.tz
import dateutil.parser
import os


class TumblrClient(object):

	def __init__(self):
		self.client = pytumblr.TumblrRestClient(
			get_env_variable('PYTUMBLR_CONSUMER_KEY'),
			get_env_variable('PYTUMBLR_CONSUMER_SECRET'),
			get_env_variable('PYTUMBLR_OAUTH_TOKEN'),
			get_env_variable('PYTUMBLR_OAUTH_SECRET')
		)
		
	def fetch(self, keyword):
	    #print self.client.tagged(keyword)
	    results = self.client.tagged(keyword)
	    for item in results:
	        create_blog(item)


def process_caption(blog):
    if 'caption' in blog:
        caption =  blog['caption']
    elif 'title' in blog:
        caption = blog['title']
    else:
        caption = "Default"
    if caption == 'null' or caption==None:
        caption = "Default"
    if len(caption) > 500:
        caption = caption[:00]
    return caption
    
def check_exist(value):
    flag = 0
    blog = Blog.objects.filter(url = value)
    if len(blog) > 0:
        flag = 1
    return flag

def create_blog(blog):
    photo_url = blog['photos'][0]['alt_sizes'][-1]['url'] if 'photos' in blog else "example.com"
    caption = process_caption(blog)
    flag = check_exist(blog['post_url'])
    if flag is 0:
        created = Blog.objects.create(
            caption = caption,
            url = blog['post_url'],
            pub_date = parsedate(blog['date']),
            img_url = photo_url
        )
        created.tags.add(*(blog['tags']))
        
    
def parsedate(datestr):
    dt = dateutil.parser.parse(datestr)
    
    if dt.tzinfo:
        dt = dt.astimezone(dateutil.tz.tzlocal()).replace(tzinfo=None)
        
    return dt    

		
def get_env_variable(var_name):
    """Get the environment variable or return exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
    raise ImproperlyConfigured(error_msg)