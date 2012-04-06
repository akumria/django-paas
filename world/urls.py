from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('world.views',
    url(r'', 'home', name='home'),
)
