from django.contrib import admin
from blog.models import Topic, Post, UserProfile

# Register your models here.


admin.site.register(Topic)
admin.site.register(Post)
admin.site.register(UserProfile)
