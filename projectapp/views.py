from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin


class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'about.html')


class AgentView(View):
    def get(self, request):
        return render(request, 'property-agent.html')


class PropertyListView(View):
    def get(self, request):
        return render(request, 'property-list.html')


class PropertyTypeView(View):
    def get(self, request):
        return render(request, 'property-type.html')


class Error404View(View):
    def get(self, request):
        return render(request, '404.html')


class ThankYouView(View):
    def get(self, request):
        return render(request, 'thankyou.html')
