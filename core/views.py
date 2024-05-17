from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import TemplateView
from django.views import View


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


