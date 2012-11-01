from django.conf.urls import patterns, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('tasks.views',
    url(r'^$', 'home', name='taskshome'),
    # url(r'^add/$', 'add_new', name='add_new_task'),
)
