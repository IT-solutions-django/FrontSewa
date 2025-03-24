from django.contrib import admin
from .models import Video, ShortVideo, Youtube

admin.site.register(Youtube)
admin.site.register(Video)
admin.site.register(ShortVideo)
