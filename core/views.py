from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from projectapp.models import City, Category, Address, Apartment, SellType


class IndexView(View):
    def get(self, request):
        city = City.objects.all()
        category = Category.objects.all()
        address = Address.objects.all()
        apartment = Apartment.objects.all()
        selltype = SellType.objects.all()

        search = request.GET.get('search')
        if not search:
            context = {
                'city': city,
                'category': category,
                'address': address,
                'apartment': apartment,
                'selltype': selltype
            }
        else:
            apartment = Apartment.objects.filter(short_name__icontains=search)
            if not apartment:
                return redirect('error404')
            else:
                context = {
                    'city': city,
                    'category': category,
                    'address': address,
                    'apartment': apartment,
                    'selltype': selltype
                }
                return render(request, 'index.html', context)
        context = {
            'city': city,
            'category': category,
            'address': address,
            'apartment': apartment,
            'selltype': selltype
        }
        return render(request, 'index.html', context)


# index view uchun post patch put delete uchun mos ish bajarishiga togri keladigan topshiriqlar mavjud emas




