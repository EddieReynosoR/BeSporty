from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from items.models import Items

# Create your views here.

class HomePage(TemplateView):
    template_name = "pages/home.html"

class ProductsPage(ListView):
    template_name = "pages/checkProducts.html"
    model = Items
