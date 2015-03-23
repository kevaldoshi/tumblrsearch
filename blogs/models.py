from django.db import models
from django.core.validators import URLValidator
from taggit.managers import TaggableManager

# Create your models here.

class Blog(models.Model):
    caption = models.CharField(max_length=500)
    url = models.URLField("A Tumblr Blog URL", max_length=250, unique=True, validators=[URLValidator()])
    pub_date = models.DateTimeField()
    img_url = models.URLField("A Tumblr Blog Image URL", max_length=250, validators=[URLValidator()])
    tags = TaggableManager()
    
    
