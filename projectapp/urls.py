from django.contrib import admin
from django.urls import path, include
from .views import ThankYouView, PropertyListView, PropertyTypeView
from .views import Error404View, AboutView, AgentView, DetailView


urlpatterns = [
    path('agents/', AgentView.as_view(), name='agents'),
    path('thank/', ThankYouView.as_view(), name='thank'),
    path('property/', PropertyListView.as_view(), name='property'),
    path('about/', AboutView.as_view(), name='about'),
    path('error404/', Error404View.as_view(), name='error404'),
    path('types/', PropertyTypeView.as_view(), name='types'),
    path('property/<int:id>', DetailView.as_view(), name='details')
]
