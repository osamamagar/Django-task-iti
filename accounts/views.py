from django.shortcuts import render , redirect
from django.views.generic.edit import CreateView
from django.contrib.auth.models import  User
from accounts.forms import  CustomizedUserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserChangeForm , PasswordChangeForm
from products.models import Product

# Create your views here.

def profile(request):
    return redirect('/products/home')



class CreateCustomUser(CreateView):
    model = User
    template_name = 'accounts/registeration.html'
    form_class = CustomizedUserCreationForm
    success_url = reverse_lazy("login")



@login_required
def profile_view(request):
    user = request.user
    user_data = Product.objects.filter(created_by=user)

    return render(request, 'accounts/profile.html', {'user': user, 'user_data': user_data})

# @login_required
# def edit_profile_view(request):
#     user = request.user

#     if request.method == 'POST':
#         profile_form = CustomizedUserCreationForm(request.POST, instance=user.profile)
#         if profile_form.is_valid():
#             profile_form.save()
#             messages.success(request, 'Profile updated successfully.')
#             return redirect('profile')
#         else:
#             messages.error(request, 'Profile update failed. Please correct the errors.')

#     return render(request, 'accounts/edit_profile.html', {'user': user})
@login_required
def edit_profile(request):
    user = request.user
    user_form = CustomizedUserCreationForm(instance=user)
    password_form = PasswordChangeForm(user)

    if request.method == 'POST':
        if 'user_form_submit' in request.POST:
            user_form = CustomizedUserCreationForm(request.POST, instance=user)
            if user_form.is_valid():
                user_form.save()
                return redirect('profile')
        elif 'password_form_submit' in request.POST:
            password_form = PasswordChangeForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect('profile')

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'password_form': password_form
    })


# @login_required
# def delete_profile_view(request):
#     user = request.user

#     if request.method == 'POST':
#         user.delete()
#         logout(request)
#         messages.success(request, 'Your profile has been deleted successfully.')
#         return redirect('login')

#     return render(request, 'accounts/delete_profile.html', {'user': user})
@login_required
def delete_profile(request):
    if request.method == 'POST':
        request.user.delete()  
        return redirect('logout')  
    return render(request, 'accounts/delete_profile.html')
