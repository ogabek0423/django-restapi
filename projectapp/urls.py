from django.contrib import admin
from django.urls import path, include
from .views import ThankYouView, PropertyListView, PropertyTypeView, TestEmoNialView
from .views import Error404View, ContactView, AboutView, AgentView


urlpatterns = [
    path('thank/', ThankYouView.as_view(), name='thank'),
    path('property/', PropertyListView.as_view(), name='property_list'),
    path('agents/', AgentView.as_view(), name='agents'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('test/', TestEmoNialView.as_view(), name='test'),
    path('error404/', Error404View.as_view(), name='error'),
    path('types/', PropertyTypeView.as_view(), name='types'),

]
