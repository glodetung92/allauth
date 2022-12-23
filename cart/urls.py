from django.urls import path
from .views import HomeView, ProductDetail, ProductSearch
from . import views

app_name = 'product'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('product-detail/<int:pk>', ProductDetail.as_view(), name='product_detail'),
    path('product-search/', ProductSearch.as_view(),name='product_search'),
   ]