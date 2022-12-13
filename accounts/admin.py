from django.contrib import admin
from .models import Type, CustomUser

admin.site.register(CustomUser)
admin.site.register(Type)
