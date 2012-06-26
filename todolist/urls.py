from django.conf.urls import patterns, include, url

from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication

from manager.api import TodoItemHandler


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'todolist.manager.views.index', name='index'),
    url(r'^register$', 'todolist.manager.views.register', name='register'),
    # url(r'^todolist/', include('todolist.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    (r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)


auth = HttpBasicAuthentication(realm="API Realm")
todoapiresource = Resource(TodoItemHandler, authentication=auth)
urlpatterns += patterns('',
   url(r'^api/items$', todoapiresource),
   url(r'^api/item/(?P<todoitem_id>[^/]+)?$', todoapiresource),
)

