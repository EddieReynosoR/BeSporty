from django.urls import path
from .views import HomePage, ProductsPage

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('catalog/', ProductsPage.as_view(), name="products"),
]