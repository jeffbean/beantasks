from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'beantasks.views.home', name='home'),
    url(r'^about$', 'beantasks.views.about', name='about'),
    # url(r'^beantasks/', include('beantasks.foo.urls')),
    url(r'^bootstrap/$', 'tasks.views.bootstrap', name='bootstrap'),
    url(r'^tasks/', include('tasks.urls', namespace='tasks')),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),


    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls), name='django-admin'),
)

urlpatterns += patterns('',

    url(r'^register/$', 'accounts.views.NewUserRegistration'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html' }),
    url(r'^logout/$', 'accounts.views.logout_page', name='bean_logout'),
    url(r'^profile/$', 'accounts.views.user_home', name='user_home'),


    url(r'^change_password/$', 'django.contrib.auth.views.password_change',
        {'template_name': 'change_password.html'}, name='change_passwd'),
    url(r'^accounts/change_password_done/$', 'django.contrib.auth.views.password_change_done',
        {'template_name': 'change_password_done.html'}, name='change_passwd_done'),

    url(r'^reset_password_done/$', 'django.contrib.auth.views.password_reset_done',
        name='reset_passwd_done'),
    url(r'^reset_password/$', 'django.contrib.auth.views.password_reset', {'template_name': 'bean_registration/password_reset_form.html'}, name='reset_passwd'),

    url(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm',
        name='reset_passwd_confirm'),

    url(r'^reset_done/$', 'django.contrib.auth.views.password_reset_complete',
        name='reset_passwd_complete'),
)


if settings.DEBUG:
    urlpatterns += patterns('',
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
         'document_root': settings.MEDIA_ROOT,
     }),
)
