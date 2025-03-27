from django.urls import path
from . import views

urlpatterns = [
    path('add_product/', views.AddProductView.as_view(), name='add_product'),
    path('products_list/', views.ProductsListView.as_view(), name='products_list'),
    path('products_list/<int:id>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('products_list/<int:id>/update/', views.UpdateProductView.as_view(), name='product_update'),
    path('products_list/<int:id>/delete/', views.DeleteProductView.as_view(), name='product_delete'),
    path('search_product/', views.SearchProductsView.as_view(), name='search_product'),
]