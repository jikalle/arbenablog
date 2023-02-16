from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)
    list_display = ('title', 'slug', 'status', 'timestamp')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'post', 'timestamp', 'active')
    list_filter = ('active', 'timestamp')
    search_fields = ('name', 'email', 'text')
    actions = ['approve_comments']
    
    def approve_comments(self, request, queryset):
        queryset.update(active=True)

admin.site.register(Post, PostAdmin)
# admin.site.register(Comment)