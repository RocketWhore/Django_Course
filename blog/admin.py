
from django.contrib import admin

from blog.models import Blog

# admin.site.register(Product)
# admin.site.register(Category)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'preview', 'body', )
