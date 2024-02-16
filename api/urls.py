from django.contrib import admin
from django.urls import path, include
from .views import EventBookingView, SponsorshipRequestView


urlpatterns = [
    path('newsletter/', include('newsletter.urls')),
    path('book-event/', EventBookingView.as_view(), name='event-booking'),
    path('sponsorship/', SponsorshipRequestView.as_view(), name='sponsorship-request'),
]
