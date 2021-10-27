from django.contrib import admin
from .models import DeviceID,Like,Comment,Share,News
# Register your models here.
admin.site.register(DeviceID)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Share)
admin.site.register(News)
