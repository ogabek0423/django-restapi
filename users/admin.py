from django.contrib import admin
from .models import Agents, Problems, Comments

admin.site.register([Agents, Problems, Comments])
