from django.conf.urls import patterns, url, include
from mysite.blog.views import archive

urlpatterns = patterns('',
    url(r'^$', archive),
)