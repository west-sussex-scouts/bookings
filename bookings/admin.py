from django.contrib import admin
from .models import Event, Location, Address


class EventAdmin(admin.ModelAdmin):
    filter_horizontal = ['attendees']

admin.site.register(Event, EventAdmin)
admin.site.register(Location)
admin.site.register(Address)