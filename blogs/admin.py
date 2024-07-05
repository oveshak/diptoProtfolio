from django.contrib import admin

from blogs.models import BlogItem, Blogs
from solo.admin import SingletonModelAdmin

# Register your models here.
admin.site.register(BlogItem)
admin.site.register(Blogs,SingletonModelAdmin)