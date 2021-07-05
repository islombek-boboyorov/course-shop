from django.contrib import admin

# Register your models here.
from shop.models import Video, Items

admin.site.register(Video)
admin.site.register(Items)