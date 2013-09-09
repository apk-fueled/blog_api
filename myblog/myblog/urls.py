from django.conf.urls import patterns, include, url
from tastypie.api import Api
from blog.api import UserResource, TagResource, PostResource, CommentResource, LogResource

blog_api = Api(api_name = 'blog')
blog_api.register(PostResource())
blog_api.register(CommentResource())
blog_api.register(UserResource())
blog_api.register(TagResource())
blog_api.register(LogResource())

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^myblog/', include('myblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^api/', include(blog_api.urls))
)