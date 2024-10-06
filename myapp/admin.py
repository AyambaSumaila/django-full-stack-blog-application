from django.contrib import admin
from .models import Post, Comment
# Register your models here.



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'status', 'publish']
    list_filter = ['created', 'publish', 'author', 'status']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status','publish']    
    raw_id_fields=['author']
    show_facets = admin.ShowFacets.ALWAYS 
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created', 'active']
    list_filter = ['created', 'active', 'updated']
    search_fields = ['name', 'email', 'body']
    
    
    