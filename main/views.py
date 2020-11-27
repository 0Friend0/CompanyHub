from django.shortcuts import render, redirect
from openpyxl import load_workbook
from .models import Product, Supplier
from django.views.generic import ListView, CreateView
from .forms import UploadFileForm


def home(request):

    return render(request, 'main/home.html', {})



def about(request):

    return render(request, 'main/about.html')


class DatabaseListView(ListView):
    model = Product
    template_name = 'main/database.html'
    context_object_name = 'product'


class ProductCreateView(CreateView):
    model = Product
    fields = ['product_code', 'name', 'supplier_name', 'price']
    template_name = 'main/database-create-product.html'

class SupplierCreateView(CreateView):
    model = Supplier
    fields = ['supplier_name', 'email']
    template_name = 'main/database-create-supplier.html'

def database_upload(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        print("hello!!!")

        wb = load_workbook(filename=request.FILES['master-file'].file)
        print(wb.sheetnames)

        return redirect('main-database')
    else:
        return render(request, 'main/database-upload-file.html', {})
