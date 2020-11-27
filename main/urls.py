from django.urls import path
from . import views
from .views import DatabaseListView, ProductCreateView, SupplierCreateView

urlpatterns = [
    path('', views.home, name='main-home'),
    path('about/', views.about, name='main-about'),
    path('database/', DatabaseListView.as_view(), name='main-database'),
    path('database/create/product', ProductCreateView.as_view(), name='main-database-create-product'),
    path('database/create/supplier', SupplierCreateView.as_view(), name='main-database-create-supplier'),
    path('database/upload', views.database_upload, name='main-database-upload-file'),

    ]