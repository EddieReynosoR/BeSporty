from django.urls import path
from .views import ItemsListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path('', ItemsListView.as_view(), name = 'list'),
    path('<int:pk>/', ItemDetailView.as_view(), name='detail'),
    path('create/', ItemCreateView.as_view(), name="create"),
    path('<int:pk>/edit/', ItemUpdateView.as_view(), name="edit"),
    path('<int:pk>/delete/', ItemDeleteView.as_view(), name="delete"),
]