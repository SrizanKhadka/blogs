from django.contrib import admin
from blog.models import Blogs,Category, Comments

# Register your models here.

admin.site.register(Blogs)
admin.site.register(Category)
admin.site.register(Comments)