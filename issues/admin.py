from django.contrib import admin
from .models import Issue, Status

# Register your models here.
admin.site.register(Issue)
admin.site.register(Status)