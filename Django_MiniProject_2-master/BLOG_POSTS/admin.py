from django.contrib import admin
from BLOG_POSTS.models import login
from BLOG_POSTS.models import createblog
# Register your models here.
admin.site.register(login)
admin.site.register(createblog)