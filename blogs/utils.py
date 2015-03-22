from django.core.exceptions import ImproperlyConfigured
import pytumblr
import json

class TumblrClient(object):

	def __init__(self):
		slef.client = pytumblr.TumblrRestClient(
			get_env_variable('pytumblr_consumer_key'),
			get_env_variable('pytumblr_consumer_secret'),
			get_env_variable('pytumblr_outh_token'),
			get_env_variable('pytumblr_outh_secret')
		)
		
	def fetch(self, keyword):
	    

		
def get_env_variable(var_name):
    """Get the environment variable or return exception"""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
    raise ImproperlyConfigured(error_msg)