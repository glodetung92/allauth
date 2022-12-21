from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Product

class HomeView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'cart/index.html'
    
    def get_context_data(self, **kwargs):
        products = Product.objects.filter(is_available=True)
        context = super().get_context_data(**kwargs)
        context['products'] = products
        return context
        

class ProductDetail(DetailView):
    model = Product
    template_name = 'cart/detail.html'
    context_object_name = 'product'