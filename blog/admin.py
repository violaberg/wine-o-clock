from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Admin configuration for managing blog posts.

    Attributes:
        list_display: Fields to be displayed in the list view.
        search_fields: Fields to be searched in the admin interface.
        list_filter: Filters for narrowing down the list of posts.
        prepopulated_fields: Fields automatically populated based on other fields.
        summernote_fields: Fields using Summernote WYSIWYG editor.
    """

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Comment)