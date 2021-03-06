from .models import Blog
from django.utils.html import strip_tags
from tumblrsearch.settings import get_env_variable
import pytumblr
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
	    results = self.client.tagged(keyword)
	    for item in results:
	        create_blog(item)


def process_caption(blog):
    if 'caption' in blog:
        caption =  blog['caption']
    elif 'title' in blog:
        caption = blog['title']
    else:
        caption = "Just Another Tumblr Blog"
    if caption in ['null', None, '']:
        caption = "Just Another Tumblr Blog"
    if len(caption) > 500:
        caption = caption[:500]
    
    caption = strip_tags(caption)
    
    return caption
    
def create_blog(blog):
    photo_url = blog['photos'][0]['alt_sizes'][-1]['url'] if 'photos' in blog else ""
    caption = process_caption(blog)

    created = Blog.objects.create(
        caption = caption,
        url = blog['post_url'],
        pub_date = parsedate(blog['date']),
        img_url = photo_url
    )
    created.tags.add(*(blog['tags']))
        
    
def parsedate(datestr):
    dt = dateutil.parser.parse(datestr)
    
    if not dt.tzinfo:
        dt = dt.astimezone(dateutil.tz.tzlocal()).replace(tzinfo='UTC')
        
    return dt    