from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.

from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length = 100)
	slug = models.SlugField(unique = True)
	text = models.TextField()
	created_on = models.DateTimeField(auto_now_add = True)
	author = models.ForeignKey(User, unique = True)

	class Meta:
		ordering = ['-created_on']

	def __unicode__(self):
		return self.slug

	def get_absolute_url(self):
		return reverse('blog.views.post', args = [self.slug])


class Comment(models.Model):
	name = models.CharField(max_length = 42)
	email = models.EmailField(max_length = 75)
	website = models.URLField(max_length = 200, null = True, blank = True)
	text = models.TextField()
	post = models.ForeignKey(Post)
	created_on = models.DateTimeField(auto_now_add = True)


	def __unicode__(self):
		return self.text

class Tag(models.Model):
	text = models.CharField(max_length = 20, primary_key = True)
	post = models.ForeignKey(Post, null = True)
	
	def __unicode__(self):
		return self.text
