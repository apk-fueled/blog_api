from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from tastypie.authentication import BasicAuthentication
from django.contrib.auth.models import User
from django.contrib.admin.models import LogEntry

from tastypie import fields

from blog.models import Post, Comment, Tag

class UserResource(ModelResource):
	post = fields.ToManyField('blog.api.PostResource', 'post_set', full = True)
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['password']
		authorization= Authorization()
		#authentication = BasicAuthentication()


class PostResource(ModelResource):
	author = fields.ForeignKey(UserResource, 'author')
	comment = fields.ToManyField('blog.api.CommentResource', 'comment_set')
	tag = fields.ToManyField('blog.api.TagResource', 'tag_set')
	class Meta:
		queryset = Post.objects.all()
		resource_name = 'post'
		authorization= Authorization()
		# authentication = BasicAuthentication()
		

class CommentResource(ModelResource):
	post = fields.ForeignKey(PostResource, 'post')
	class Meta:
		queryset = Comment.objects.all()
		resource_name = 'comment'
		authorization= Authorization()
		#authentication = BasicAuthentication()

class TagResource(ModelResource):
	post = fields.ForeignKey(PostResource, 'post')
	class Meta:
		queryset = Tag.objects.all()
		authorization= Authorization()


class LogResource(ModelResource):
	class Meta:
		queryset = LogEntry.objects.all();
		resource_name = "log"