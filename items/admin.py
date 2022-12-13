from django.contrib import admin
from .models import Items, Type, Size

# Register your models here.

admin.site.register(Items)
admin.site.register(Type)
admin.site.register(Size)