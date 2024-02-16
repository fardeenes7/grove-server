from django.contrib import admin
from django.urls import path, include
from .views import SubscriberView

urlpatterns = [
    path('subscribe/', SubscriberView.as_view(), name='subscribe'),
]
