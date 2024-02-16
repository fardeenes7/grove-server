from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')
    ordering = ('-date',)

admin.site.register(Subscriber, SubscriberAdmin)