from telnetlib import LOGOUT
from django.http import HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import render ,get_object_or_404 ,redirect
from django.urls import reverse
from .models import Product 
from sections.models import Section
from .forms import ProductForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages







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

# @login_required()
# def delete(request, id):
#     product = Product.objects.get(id=id)
#     product.delete()    
#     url = reverse('products:home')
#     return redirect(url)

@login_required
def delete(request, id):
    product = get_object_or_404(Product, id=id)

    # Check if the user is the owner of the product
    if product.created_by != request.user:
        return HttpResponseForbidden("You do not have permission to delete this product.")

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

        section_id = request.POST.get('section_id')
        if section_id:
            try:
                section = Section.objects.get(pk=section_id)
                addProduct.section = section
            except Section.DoesNotExist:
                return HttpResponseBadRequest("Invalid section ID")


        addProduct.created_by = request.user
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


# @login_required()
# def edit_product(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES, instance=product)
#         if form.is_valid():
#             form.save()
#             return redirect('products:product_detail', product.id)
#     else:
#         form = ProductForm(instance=product)

#     return render(request, 'products/edit_product.html', {'form': form, 'product': product})

@login_required
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the user is the owner of the product
    if product.created_by != request.user:
        return HttpResponseForbidden("You do not have permission to edit this product.")

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products:product_detail', product.id)
    else:
        form = ProductForm(instance=product)

    return render(request, 'products/edit_product.html', {'form': form, 'product': product})


@login_required
def profile_view(request):
    user = request.user  
    return render(request, 'profile.html', {'user': user})

@login_required
def edit_profile_view(request):
    user = request.user

    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
        else:
            messages.error(request, 'Profile update failed. Please correct the errors.')

    return render(request, 'edit_profile.html', {'user': user})

@login_required
def delete_profile_view(request):
    user = request.user

    if request.method == 'POST':
        user.delete()
        LOGOUT(request)
        messages.success(request, 'Your profile has been deleted successfully.')
        return redirect('login')

    return render(request, 'delete_profile.html', {'user': user})
