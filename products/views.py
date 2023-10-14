from django.http import HttpResponseBadRequest
from django.shortcuts import render ,get_object_or_404 ,redirect
from django.urls import reverse
from .models import Product 
from sections.models import Section
from .forms import ProductForm
from django.contrib.auth.decorators import login_required




def contact_us(request):
    return render(request, 'products/contact_us.html')

def about_us(request):
    return render(request, 'products/about_us.html')


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    related_products = Product.objects.filter(section=product.section).exclude(id=id)
    

    return render(request, 'products/product_detail.html', {'product': product, 'related_products': related_products})



def Home(request):
    products = Product.objects.all().order_by('id')
    return render(request, 'products/homepage.html',context={"products":products})

@login_required()
def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()    
    url = reverse('products:home')
    return redirect(url)


def search(request):
    query = request.GET.get('q', '') 
    products = Product.objects.filter(name__icontains=query)  
    return render(request, 'products/search.html', {'products': products, 'query': query})
 
@login_required()
def create_product(request):
    sections = Section.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        if not name or not price:
            return render(request, 'products/create_product.html')

        try:
            price = float(price)
        except ValueError:
            return render(request, 'products/create_product.html')

        addProduct = Product()
        addProduct.name = name
        addProduct.price = price
        addProduct.description = description
        addProduct.image = image

        # Check if a section is specified in the form.
        section_id = request.POST.get('section_id')
        if section_id:
            try:
                section = Section.objects.get(pk=section_id)
                addProduct.section = section
            except Section.DoesNotExist:
                return HttpResponseBadRequest("Invalid section ID")

        addProduct.save()

        url = reverse('products:product_detail', args=[addProduct.id])
        return redirect(url)
    else:
        return render(request, 'products/create_product.html', {'sections': sections})


# def create_product(request, section_id):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             # Assuming your form includes fields for name, price, and description
#             name = form.cleaned_data['name']
#             price = form.cleaned_data['price']
#             description = form.cleaned_data['description']

#             # Create a new product and associate it with the section
#             product = Product(name=name, price=price, description=description, section_id=section_id)
#             product.save()

#             return redirect('products:product_detail', product.id)
#     else:
#         form = ProductForm()

#     return render(request, 'products/create_product.html', {'form': form})


@login_required()
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_detail', product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})
