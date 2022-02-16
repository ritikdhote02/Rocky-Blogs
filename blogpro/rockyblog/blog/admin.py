from django.contrib import admin
from .models import Category,Post


# For configuration of categories admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'description', 'url', 'add_date',)
    search_fields = ('title',)
    list_filter = ('add_date',)
    list_per_page = 50

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'cat', 'url', 'add_date',)
    search_fields = ('title',)
    list_filter = ('cat', 'add_date',)
    list_per_page = 50






admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

