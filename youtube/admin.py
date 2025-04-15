from django.contrib import admin
from .models import Video, ShortVideo, Youtube, ReviewVideo

admin.site.register(Youtube)
admin.site.register(Video)
admin.site.register(ShortVideo)
admin.site.register(ReviewVideo)
