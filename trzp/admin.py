from django.contrib import admin
from .models import Products , Laptop , Computer , GameConsole

# Register your models here.

admin.site.register(Products)
admin.site.register(Laptop)
admin.site.register(Computer)
admin.site.register(GameConsole)