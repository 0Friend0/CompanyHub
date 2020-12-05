from django.urls import path
from . import views
from .views import (DatabaseProductListView, DatabaseSupplierListView, ProductCreateView,
                    SupplierCreateView, ProductDetailView, SupplierDetailView,
                    ProductUpdateView, SupplierUpdateView, SearchProductListView,
                    SearchSupplierListView, ProductDeleteView, SupplierDeleteView
                    )

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('database/product', DatabaseProductListView.as_view(), name='main-database-product'),
    path('database/supplier', DatabaseSupplierListView.as_view(), name='main-database-supplier'),
    path('database/create/product', ProductCreateView.as_view(), name='main-database-create-product'),
    path('database/create/supplier', SupplierCreateView.as_view(), name='main-database-create-supplier'),
    path('product/<pk>', ProductDetailView.as_view(), name='main-product-detail'),
    path('supplier/<pk>', SupplierDetailView.as_view(), name='main-supplier-detail'),
    path('product/<pk>/update', ProductUpdateView.as_view(), name='main-update-product'),
    path('supplier/<pk>/update', SupplierUpdateView.as_view(), name='main-update-supplier'),
    path('product/<pk>/delete', ProductDeleteView.as_view(), name='main-delete-product'),
    path('supplier/<pk>/delete', SupplierDeleteView.as_view(), name='main-delete-supplier'),
    path('database/upload', views.database_upload, name='main-database-upload-file'),
    path('database/search_product', SearchProductListView.as_view(), name='main-search-product'),
    path('database/search_supplier', SearchSupplierListView.as_view(), name='main-search-supplier'),


    ]