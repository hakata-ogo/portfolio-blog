from django.contrib import admin
from .models import Post,Category

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''

    list_display = ('title', 'created_on', 'last_modified',)
    list_filter = ('created_on', 'title',)
    search_fields = ('title','categories__name', 'body',)
    ordering = ('-created_on', 'title')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)
