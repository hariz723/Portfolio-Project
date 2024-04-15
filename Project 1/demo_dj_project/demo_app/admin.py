from django.contrib import admin

# Register your models here.
from demo_app.models import AppUser, Article

# Register your models here.

admin.site.register(AppUser)
admin.site.register(Article)

