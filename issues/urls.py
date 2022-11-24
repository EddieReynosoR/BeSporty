
from django.urls import path
from .views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView

urlpatterns = [
    path('', IssueListView.as_view(), name='listIssue'),
    path('<int:pk>/', IssueDetailView.as_view(), name='detailIssue'),
    path('createIssue/', IssueCreateView.as_view(), name="createIssue"),
    path('<int:pk>/editIssue/', IssueUpdateView.as_view(), name="editIssue"),
    path('<int:pk>/deleteIssue/', IssueDeleteView.as_view(), name="deleteIssue"),
    path('', IssueListView.as_view(), name='listIssue'),
]
