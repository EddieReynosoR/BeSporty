

from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Items, Type
from django.http import JsonResponse
from .carritos import Cart
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
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

def search_results(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        res = None
        item = request.POST.get('item')
        qs = Items.objects.filter(title__icontains = item)   
        if len(qs)>0 and len(item)>0:
            data = []
            for pos in qs:
                item = {
                    'pk': pos.pk,
                    'title': pos.title,
                    'type': pos.type.name,
                    'image': str(pos.image.url)
                }
                data.append(item)
            res = data
        else:
            res = 'No items found ...'
        return JsonResponse({'data': res})
    return JsonResponse({})

#Cart functions
def store(request):
    itemsCart = Items.objects.all()
    return render(request, "base.html", {'items': itemsCart})

def addItem(request, item_id):
    size = request.POST.get("size")
    quantity = request.POST.get("quantity")

    if quantity is None:
        quantity = 1

    cart = Cart(request)
    item = Items.objects.get(id=item_id)
    if len(cart.cart.keys()) < 10:
        cart.add(item,size,quantity)
    else:
        messages.success(request, "You can't add more items to your cart.")
        return redirect('cart')
    return redirect('cart')

def deleteItem(request, item_id):
    key = request.POST.get("key")
    cart = Cart(request)
    cart.delete(key)
    return redirect("cart")

def substractItem(request, item_id):
    key = request.POST.get("key")
    cart = Cart(request)
    item = Items.objects.get(id=item_id)
    cart.substractItem(item, key)
    return redirect("cart")

def clean(request):
    cart = Cart(request)
    cart.clean()
    return redirect("cart")

class CartPage(TemplateView):
    template_name = "items/cart.html"

def buyConfirm(request):
    user = request.user
    send_mail(
        'Thank you for your purchase',
        f'We are glad that you have buy with us!, hope you comeback!',
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )
    clean(request)

    return render(request, 'registration/token4.html', {})


