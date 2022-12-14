
from django.urls import path
from .views import IssueListView, IssueDetailView, IssueCreateView, IssueUpdateView, IssueDeleteView, contact

urlpatterns = [
    path('', IssueListView.as_view(), name='listIssue'),
    path('<int:pk>/', IssueDetailView.as_view(), name='detailIssue'),
    path('createIssue/', contact, name="createIssue"),
    path('<int:pk>/editIssue/', IssueUpdateView.as_view(), name="editIssue"),
    path('<int:pk>/deleteIssues/', IssueDeleteView.as_view(), name="deleteIssues"),
    path('', IssueListView.as_view(), name='listIssue'),
]
