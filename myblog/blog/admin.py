from django.contrib import admin
from blog.models import Tag, Post, Comment
	
class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'author']
	#fields = (('title', 'author'), 'slug')	

class CommentAdmin(admin.ModelAdmin):
	list_display = ['name', 'post']

class TagAdmin(admin.ModelAdmin):
	list_display = ['text', 'post']


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
