from django.urls import path
from . import views
from .views import DatabaseProductListView, DatabaseSupplierListView, ProductCreateView, SupplierCreateView, ProductDetailView, SupplierDetailView

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('database/product', DatabaseProductListView.as_view(), name='main-database-product'),
    path('database/supplier', DatabaseSupplierListView.as_view(), name='main-database-supplier'),
    path('database/create/product', ProductCreateView.as_view(), name='main-database-create-product'),
    path('database/create/supplier', SupplierCreateView.as_view(), name='main-database-create-supplier'),
    path('product/<pk>', ProductDetailView.as_view(), name='main-product-detail'),
    path('supplier/<pk>', SupplierDetailView.as_view(), name='main-supplier-detail'),
    path('database/upload', views.database_upload, name='main-database-upload-file'),

    ]