from re import search
from django.contrib import admin

# Register your models here.

from . models import Post , Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created_date','status')
    list_filter =  ('title','author','status')
    search_fields = ('title','slug')
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name','email','created_date','active')
    list_filter =  ('name','email','active')
    search_fields = ('comment',)
    
    
admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)