from django.conf import settings
from django.core.cache import cache

from blog.models import Blog


def get_cache_version_for_blog(blog_pk):
    if settings.CACHE_ENABLED:
        key = f'blog_list{blog_pk}'
        blog_list = cache.get(key)
        if blog_list is None:
            blog_list = Blog.objects.filter(blog__pk=blog_pk)
            cache.set(key, blog_list)
    else:
        blog_list = Blog.objects.filter(blog__pk=blog_pk)
    return blog_list