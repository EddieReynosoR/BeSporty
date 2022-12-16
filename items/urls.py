from django.urls import path

from .views import ItemsListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, SneakersListView, JerseysListView, ExerciseListView, SportListView,addItem, deleteItem, substractItem, clean, CartPage,search_results, buyConfirm


urlpatterns = [
    path('', ItemsListView.as_view(), name = 'list'),
    path('Sneakers/', SneakersListView.as_view(), name = 'list_sneakers'),
    path('Exercises/', ExerciseListView.as_view(), name = 'list_exercise'),
    path('Sports/', SportListView.as_view(), name = 'list_sport'),
    path('Jerseys/', JerseysListView.as_view(), name = 'list_jerseys'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name="create"),
    path('<int:pk>/edit/', ItemUpdateView.as_view(), name="edit"),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name="delete"),
    path('search/', search_results, name='search'),
    path('Sneakers/items/search/', search_results, name="search"),
    path('Sneakers/items/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('Exercises/items/search/', search_results, name="search"),
    path('Exercises/items/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('Sports/items/search/', search_results, name="search"),
    path('Sports/items/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('Jerseys/items/search/', search_results, name="search"),
    path('Jerseys/items/<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('add/<int:item_id>', addItem, name="add"),
    path('remove/<int:item_id>', deleteItem, name="remove"),
    path('subtract/<int:item_id>', substractItem, name="substract"),
    path('clean/', clean, name="clean"),
    path('cart/',CartPage.as_view(), name="cart"),
    path('buyConfirm/', buyConfirm, name="confirmBuy"),
]