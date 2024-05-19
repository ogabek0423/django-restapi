from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View
from projectapp.models import City, Category, Address, Apartment, SellType
from users.models import Agents, Comments, Problems


class IndexView(View):
    def get(self, request):
        city = City.objects.all()
        category = Category.objects.all()
        address = Address.objects.all()
        apartment = Apartment.objects.all()
        selltype = SellType.objects.all()
        agent = Agents.objects.all()
        comment = Comments.objects.all()
        problem = Problems.objects.all()
        search = request.GET.get('search')
        if not search:
            context = {

                'agents': agent,
                'city': city,
                'category': category,
                'address': address,
                'apartment': apartment,
                'selltype': selltype,
                'comment': comment,
                'problem': problem,
            }
        else:
            apartment = Apartment.objects.filter(short_name__icontains=search)
            category = Category.objects.filter(name__icontains=search)
            address = Address.objects.filter(name__icontains=search)
            selltype = SellType.objects.filter(name__icontains=search)
            agent = Agents.objects.filter(firstname__icontains=search)
            comment = Comments.objects.filter(comment_title__icontains=search)

            if not apartment:
                return redirect('error404')
            else:
                context = {
                    'city': city,
                    'category': category,
                    'address': address,
                    'apartment': apartment,
                    'selltype': selltype,
                    'comment': comment,
                    'problem': problem,
                    'agents': agent
                }
                return render(request, 'index.html', context)
        context = {
            'city': city,
            'category': category,
            'address': address,
            'apartment': apartment,
            'selltype': selltype,
            'comment': comment,
            'problem': problem,
            'agents': agent
        }
        return render(request, 'index.html', context)


# index view uchun post patch put delete uchun mos ish bajarishiga togri keladigan topshiriqlar mavjud emas




