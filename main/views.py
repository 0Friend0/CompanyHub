from django.shortcuts import render, redirect
from openpyxl import load_workbook
from .models import Product, Supplier
from django.views.generic import ListView, CreateView, DetailView
from .forms import UploadFileForm


def home(request):

    return render(request, 'main/home.html', {})



def about(request):

    return render(request, 'main/about.html')


class DatabaseProductListView(ListView):
    model = Product
    template_name = 'main/database-product.html'
    context_object_name = 'product'


class DatabaseSupplierListView(ListView):
    model = Supplier
    template_name = 'main/database-supplier.html'
    context_object_name = 'supplier'


class ProductCreateView(CreateView):
    model = Product
    fields = ['product_code', 'name', 'supplier_name', 'price']
    template_name = 'main/database-create-product.html'


class SupplierCreateView(CreateView):
    model = Supplier
    fields = ['supplier_name', 'email']
    template_name = 'main/database-create-supplier.html'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product-detail.html'


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'main/supplier-detail.html'

def database_upload(request):
    if request.method == "POST":
        file_form = UploadFileForm(request.POST, request.FILES)

        if file_form.is_valid() and request.FILES['master-file'].name == "Master_Upload_File.xlsx":
            header = "Product Code"
            wb = load_workbook(filename=request.FILES['master-file'].file)
            ws = wb["Product"]

            for row in ws:
                if row[0].value == header:
                    continue
                else:
                    p = Product.objects.create(product_code=row[0].value, name=row[1].value, price=row[3].value)
                    p.save()
                    s = Supplier.objects.get(supplier_name=row[2].value)
                    p = Product.objects.get(product_code=row[0].value)
                    p.supplier_name = s
                    p.save()


        return render(request, 'main/database-upload-file.html', {'file_form': file_form})
    else:
        file_form = UploadFileForm()
        return render(request, 'main/database-upload-file.html', {'file_form': file_form})
