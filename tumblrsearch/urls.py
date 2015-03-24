from django.conf.urls import patterns, include, url
from django.contrib import admin
from blogs import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tumblrsearch.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'blogs.views.index'),
    url(r'^search/', 'blogs.views.search'),
    url(r'^admin/', include(admin.site.urls)),
)
