
from django.urls import path
from .views import IssueListView, IssueDetailView, IssueCreateView


urlpatterns = [
    path('', IssueListView.as_view(), name='list2'),
    path('<int:pk>/', IssueDetailView.as_view(), name='detail'),
    path('new/', IssueCreateView.as_view(), name='new'),
]
