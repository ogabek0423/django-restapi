from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from users.forms import UserRegisterForm, UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, City, Address, Apartment, SellType
from users.models import Comments, Problems, Agents


class AboutView(LoginRequiredMixin, View):
    def get(self, request):
        agent = Agents.objects.all()
        comment = Comments.objects.all()
        context = {
            'agents': agent,
            'comments': comment,
        }
        return render(request, 'about.html', context)


class AgentView(View):
    def get(self, request):
        agent = Agents.objects.all()
        context = {
            'agents': agent
        }
        return render(request, 'property-agent.html', context)


class PropertyListView(View):
    def get(self, request):
        apartment = Apartment.objects.all()
        city = City.objects.all()
        address = Address.objects.all()
        category = Category.objects.all()
        sell_type = SellType.objects.all()
        context = {
            'apartment': apartment,
            'category': category,
            'address': address,
            'city': city,
            'sell_type': sell_type,
        }
        return render(request, 'property-list.html', context)


class PropertyTypeView(View):
    def get(self, request):
        apartment = Apartment.objects.all()
        city = City.objects.all()
        address = Address.objects.all()
        category = Category.objects.all()
        sell_type = SellType.objects.all()
        context = {
            'apartment': apartment,
            'category': category,
            'address': address,
            'city': city,
            'sell_type': sell_type,
        }
        return render(request, 'property-type.html', context)


class Error404View(View):
    def get(self, request):
        return render(request, '404.html')


class ThankYouView(View):
    def get(self, request):
        return render(request, 'thankyou.html')
