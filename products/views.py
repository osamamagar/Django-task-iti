from django.shortcuts import render ,get_object_or_404 ,redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Product 




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
        image = request.POST['image']
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

    
    

