from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Items, Type

# Create your views here.

class ItemsListView(ListView):
    template_name = "items/list.html"
    model = Items

class SneakersListView(ListView):
    template_name = "items/list.html"
    model = Items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Type.objects.get(name="Sneakers")
        context["items_list"] = Items.objects.filter(type=pending_status).reverse()
        return context

class ExerciseListView(ListView):
    template_name = "items/list.html"
    model = Items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Type.objects.get(name="Exercise")
        context["items_list"] = Items.objects.filter(type=pending_status).reverse()
        return context

class SportListView(ListView):
    template_name = "items/list.html"
    model = Items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Type.objects.get(name="Sport")
        context["items_list"] = Items.objects.filter(type=pending_status).reverse()
        return context


class JerseysListView(ListView):
    template_name = "items/list.html"
    model = Items

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pending_status = Type.objects.get(name="Jerseys")
        context["items_list"] = Items.objects.filter(type=pending_status).reverse()
        return context

class ItemDetailView(DetailView):
    template_name = "items/detail.html"
    model = Items

class ItemCreateView(CreateView):
    template_name = "items/create.html"
    model = Items
    fields = ["title", "price", "description", "image", "type"]

    def form_valid(self, form):
        form.instance.requester = self.request.user
        return super().form_valid(form)


class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "issues/edit.html"
    model = Items
    fields = ["title", "price", "description", "image"]

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "issues/delete.html"
    model = Items
    success_url = reverse_lazy("list")

    def test_func(self):
        post_obj = self.get_object()
        return post_obj.author == self.request.user


