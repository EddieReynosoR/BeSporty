from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Issue, Status
from accounts.models import CustomUser
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


class IssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue


class CompletedIssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="Completed")
        context["issue_list"] = Issue.objects.filter(
            author=self.request.user).filter(status=pending_status).order_by('created_on').reverse()
        return context


class ToDodIssueListView(ListView):
    template_name = "issues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="To do")
        context["issue_list"] = Issue.objects.filter(
            author=self.request.user).filter(status=pending_status).order_by('created_on').reverse()
        return context


class PendingIssueListView(ListView):
    template_name = "isssues/list.html"
    model = Issue

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Status.objects.get(name="Pending")
        context["issues_list"] = Issue.objects.filter(
            author=self.request.user).filter(status=pending_status).order_by('created_on').reverse()
        return context


class IssueDetailView(DetailView):
    template_name = "issues/detailIssue.html"
    model = Issue


class IssueCreateView(CreateView):
    template_name = "issues/createIssue.html"
    model = Issue
    fields = ["title", "body"]
    exclude = ["author"]
    def form_valid(self, form):

        form.instance.requester = self.request.user
        return super().form_valid(form)


class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/editIssue.html"
    model = Issue
    fields = ["title", "status", "body"]

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/deleteIssues.html"
    model = Issue
    success_url = reverse_lazy("listIssue")

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user

def contact(request):
    if request.method == "POST":
        issue_title = request.POST.get("title")
        issue_body = request.POST.get("body")

        if request.user.is_authenticated:
            user = request.user
            issue_obj = Issue.objects.create(title = issue_title, body = issue_body, author = user)
            issue_obj.save()

            user_obj = CustomUser.objects.get(username = issue_obj.author)

            

            send_mail(
                'Support Email',
                f'We received your email {user_obj.username}, please wait until we answer you!',
                settings.EMAIL_HOST_USER,
                [user_obj.email],
                fail_silently=False,
            )

            return render(request, 'issues/createIssue.html', {'issue_author': user_obj.username})
    else:
        return render(request, 'issues/createIssue.html', {})