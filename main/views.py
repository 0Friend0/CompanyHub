from django.shortcuts import render, redirect
from openpyxl import load_workbook
from .models import Product, Supplier
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UploadFileForm
from django.db.models import Q

def home(request):

    return render(request, 'main/home.html', {})


def about(request):

    return render(request, 'main/about.html')


class DatabaseProductListView(ListView):
    model = Product
    template_name = 'main/database-product.html'
    context_object_name = 'product'
    paginate_by = 2


class SearchProductListView(ListView):
    model = Product
    template_name = 'main/search-product.html'
    paginate_by = 2


    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Product.objects.filter(Q(product_code__icontains=query) | Q(name__icontains=query))

        return object_list


class DatabaseSupplierListView(ListView):
    model = Supplier
    template_name = 'main/database-supplier.html'
    context_object_name = 'supplier'
    paginate_by = 25


class SearchSupplierListView(ListView):
    model = Supplier
    template_name = 'main/search-supplier.html'
    paginate_by = 25


    def get_queryset(self):
        query = self.request.GET.get("q")
        object_list = Supplier.objects.filter(Q(supplier_name__icontains=query) | Q(email__icontains=query))

        return object_list


class ProductCreateView(SuccessMessageMixin, CreateView):
    model = Product
    fields = ['product_code', 'name', 'supplier_name', 'price']
    template_name = 'main/database-create-product.html'
    success_message = '%(name)s was created successfully!'


class SupplierCreateView(SuccessMessageMixin, CreateView):
    model = Supplier
    fields = ['supplier_name', 'email']
    template_name = 'main/database-create-supplier.html'
    success_message = '%(supplier_name)s was created successfully!'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product-detail.html'


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'main/supplier-detail.html'


class SupplierUpdateView(SuccessMessageMixin, UpdateView):
    model = Supplier
    fields = ['supplier_name', 'email']
    template_name = 'main/database-update-supplier.html'
    success_message = '%(supplier_name)s was updated successfully!'


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    model = Product
    fields = ['product_code', 'name', 'supplier_name', 'price']
    template_name = 'main/database-update-product.html'
    success_message = '%(name)s was updated successfully!'


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'main/database-delete-product.html'
    success_url = '/database/product'


class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'main/database-delete-supplier.html'
    success_url = '/database/supplier'



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

        return render(request, 'main/database-upload-file.html', {'file_form': file_form, 'upload': False})
    else:
        file_form = UploadFileForm()
        return render(request, 'main/database-upload-file.html', {'file_form': file_form})
