# from django.shortcuts import HttpResponse,render,get_object_or_404,redirect
# from products.models import Product


# Create your views here.

# def product_list(request):
#     products=Product.objects.all()
#     output=""

#     for product in products:
#         output = output +f"{product.name} - Rs. {product.price}\n"
    
#     return HttpResponse(output,content_type="text/plain")
    
    

# def product_details(request, id):
#     product = Product.objects.get(id=id)
#     output = f"{product.name}\n {product.description}\nPrice: Rs.{product.price}"
#     return HttpResponse(output,content_type="text/plain")


# def product_list(request):
#     products=Product.objects.all().order_by('-created_at')
#     return render(
#         request,
#         'products/products_list.html',
#         {'products':products}
#     )

# def product_details(request, id):
#     product = get_object_or_404(Product, id=id)
#     return render(
#         request,
#         'products/product_detail.html',
#         {'product': product}
#     )
 
 # CRUD Operation   
# # CREATE

# def product_create(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         description = request.POST['description']
#         price = request.POST['price']
#         stock = request.POST['stock']
#         Product.objects.create(
#             name=name,
#             description=description,
#             price=price,
#             stock=stock
#         )
        
#         return redirect('products:product-list')
#     return render(request, 'products/product_create.html')

# # UPDATE
# def product_update(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         product.name = request.POST['name']
#         product.description = request.POST['description']
#         product.price = request.POST['price']
#         product.stock = request.POST['stock']
#         product.save()
#         return redirect('products:product-list')
#     return render(request, 'products/product_update.html', {'product': product})



 
# from .forms import ProductForm
# from django.contrib.auth.decorators import login_required


# @login_required(login_url='users:login')
# def product_create(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('products:product-list')
#     else:
#         form = ProductForm()
    
#     return render(request, 'products/product_create.html',{'form':form})

# @login_required(login_url='users:login')
# def product_update(request,id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('products:product-list')
#     else:
#         form = ProductForm(instance=product)
#     return render(request, 'products/product_update.html',{'form':form})

# # # DELETE
# @login_required(login_url='users:login')
# def product_delete(request, id):
#     product = get_object_or_404(Product, id=id)
#     if request.method == 'POST':
#         product.delete()
#         return redirect('products:product-list')
#     return render(request, 'products/product_delete.html', {'product': product})
    

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from products.forms import ProductForm
from .models import Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ProductListView(ListView):
    model=Product
    template_name='products/products_list.html'
    context_object_name='products'
    ordering=['-created_at']
    

class ProductDetailView(DetailView):
    model = Product
    template_name='products/product_detail.html'
    context_object_name='product'
    
    
class ProductCreateView(LoginRequiredMixin,  CreateView):
    model=Product
    form_class=ProductForm
    template_name='products/product_create.html'
    success_url= reverse_lazy('products:product-list')
    login_url ='users:login'
    
class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update.html'
    success_url = reverse_lazy('products:product-list')
    login_url = 'users:login'
    
   
    
class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('products:product-list')
    login_url = 'users:login'

