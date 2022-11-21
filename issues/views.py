from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Issue, Status

# Create your views here.


class IssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue


class DraftIssueListView(ListView):
    template_name = "posts/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="draft")
        context["post_list"] = Issue.objects.filter(
            author=self.request.user).filter(status=pending_status).order_by('created_on').reverse()
        return context


class PublishedIssueListView(ListView):
    template_name = "posts/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="published")
        context["post_list"] = Issue.objects.filter(
            author=self.request.user).filter(status=pending_status).order_by('created_on').reverse()
        return context


class ArchivedIssueListView(ListView):
    template_name = "posts/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="archived")
        context["post_list"] = Issue.objects.filter(
            author=self.request.user).filter(status=pending_status).order_by('created_on').reverse()
        return context


class IssueDetailView(DetailView):
    template_name = "issues/detail.html"
    model = Issue


class IssueCreateView(CreateView):
    template_name = "issues/new.html"
    model = Issue
    fields = ["title", "body"]


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Issue
    fields = ["title", "status", "body"]

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Issue
    success_url = reverse_lazy("list")

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user
