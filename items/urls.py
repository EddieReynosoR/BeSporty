from django.urls import path
from .views import ItemsListView, ItemDetailView, ItemCreateView, ItemUpdateView, ItemDeleteView, SneakersListView, JerseysListView, ExerciseListView, SportListView

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
]