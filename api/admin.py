from django.contrib import admin
from .models import EventBooking, SponsorshipRequest

class EventBookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'company_name', 'event', 'guests', 'date', 'time', 'date_created')
    list_filter = ('date', 'time', 'date_created')
    search_fields = ('first_name', 'last_name', 'email', 'phone', 'company_name', 'event')
    ordering = ('date', 'time', 'date_created')

class SponsorshipRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'phone', 'email', 'message', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'company', 'phone', 'email', 'message')
    ordering = ('date',)

admin.site.register(EventBooking, EventBookingAdmin)
admin.site.register(SponsorshipRequest, SponsorshipRequestAdmin)