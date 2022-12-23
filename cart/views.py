from django.shortcuts import render
from django.http import HttpResponse, request
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from store.models import Product

class HomeView(LoginRequiredMixin, ListView):
    paginate_by = 3
    model = Product
    template_name = 'cart/index.html'
    context_object_name = 'products'
    

class ProductDetail(DetailView):
    model = Product
    template_name = 'cart/detail.html'
    context_object_name = 'product'

class ProductSearch(ListView):
    model = Product
    template_name = 'cart/index.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        keyword = self.request.GET.get('q')
        if keyword:
            self.queryset = Product.objects.filter(product_name__icontains=keyword)
        else:
            self.queryset = Product.objects.all()
        return super().get_queryset()