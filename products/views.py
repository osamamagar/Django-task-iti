from django.shortcuts import render ,get_object_or_404 ,redirect
from django.urls import reverse
from .models import Product 
from .forms import ProductFormEdit




def contact_us(request):
    return render(request, 'products/contact_us.html')

def about_us(request):
    return render(request, 'products/about_us.html')


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    return render(request, 'products/product_detail.html', {'product': product})



def Home(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'products/homepage.html',context={"products":products})


def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()    
    url = reverse('products:home')
    return redirect(url)


def search(request):
    query = request.GET.get('q', '') 
    products = Product.objects.filter(name__icontains=query)  
    return render(request, 'products/search.html', {'products': products, 'query': query})
 
def create_product(request):

    if request.method =='POST':
        name = request.POST['name']
        price = request.POST['price']
        description = request.POST['description']
        image = request.FILES ['image']
        if not name or not price:
            return render(request, 'products/create_product.html')
        

        try:
            price = float(price) 
        except ValueError:
            return render(request, 'products/create_product.html')



        addProduct = Product()
        addProduct.name=name
        addProduct.price=price
        addProduct.description=description
        addProduct.image=image
        addProduct.save()

        url = reverse('products:product_detail', args=[addProduct.id])
        return redirect(url)
    else:
        return render(request, 'products/create_product.html')


# def create_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)

#         if form.is_valid():
#             product = form.save()
            
#             return redirect('products:product_detail', product.id)
#         else:
#             return render(request, 'products/create_product.html', {'form': form})
#     else:
#         form = ProductForm()
#         return render(request, 'products/create_product.html', {'form': form})


def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        form = ProductFormEdit(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:home')

    else:
        form = ProductFormEdit(instance=product)

    return render(request, 'products/edit_product.html', {'product': product, 'form': form})




    

