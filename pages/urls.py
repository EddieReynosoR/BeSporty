from django.urls import path
from .views import HomePage, ProductsPage
from items.views import search_results, ItemDetailView

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('catalog/', ProductsPage.as_view(), name="products"),
    path('catalog/items/search/', search_results, name='searchBar'),
    path('catalog/items/<int:pk>/', ItemDetailView.as_view(), name='detail')
]