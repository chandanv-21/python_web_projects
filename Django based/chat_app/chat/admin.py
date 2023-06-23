from django.contrib import admin
from . models import Room, Message

# Register your models here.
admin.site.register(Room)

class HomeAdmin(admin.ModelAdmin):

    list_display=['room', 'user', 'msg', 'dates']
    list_filter = ['room', 'user']
admin.site.register(Message, HomeAdmin)
