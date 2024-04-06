from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MenuItem, Order
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import login, logout

# Views for main pages
def index(request):
    return render(request, 'my_cafe/index.html')

def contact(request):
    return render(request, 'my_cafe/contact.html')

def menu(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'my_cafe/menu.html', {'menu_items': menu_items})

def reservation(request):
    return render(request, 'my_cafe/reservation.html')

# Place Order View
@login_required
def place_order(request):
    menu_items = MenuItem.objects.all()  # Retrieve all menu items
    
    if request.method == 'POST':
        user = request.user
        menu_item_id = request.POST.get('menu_item')
        quantity = request.POST.get('quantity')
        
        menu_item = MenuItem.objects.get(pk=menu_item_id)
        
        # Save order to the database
        order = Order.objects.create(user=user, menu_item=menu_item, quantity=quantity)
        
        # Send order confirmation email using AWS SES
        subject = 'Order Confirmation'
        message = f'Hi {user.username},\n\nYour order has been successfully placed. Thank you for choosing Sahil\'s Cafe!'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = [user.email]
        send_mail(subject, message, from_email, to_email, fail_silently=True)
        
        # Redirect to menu page after successful order placement
        return redirect('menu')
    
    return render(request, 'my_cafe/place_order.html', {'menu_items': menu_items})

# Delete Order View
@login_required
def delete_order(request, order_id):
    # Get the order object
    order = Order.objects.get(id=order_id)

    # Check if the logged-in user is the owner of the order
    if request.user == order.user:
        # Delete the order
        order.delete()
        messages.success(request, 'Order deleted successfully.')
    else:
        # If the user is not the owner of the order, show an error message
        messages.error(request, 'You are not authorized to delete this order.')

    # Redirect back to the order history page
    return redirect('order_history')  # Replace 'order_history' with the appropriate URL name for your order history page

# Order History View
@login_required
def order_history(request):
    # Retrieve orders belonging to the logged-in user
    orders = Order.objects.filter(user=request.user)
    return render(request, 'my_cafe/order_history.html', {'orders': orders})

# Account-related views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to index.html after successful signup
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # Redirect to index.html after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirect to index.html after logout

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Logic for sending password reset email
            # Redirect to password_reset_done.html
            pass
    else:
        form = PasswordResetForm()
    return render(request, 'registration/password_reset.html', {'form': form})

def password_reset_complete_view(request):
    # Logic for password reset complete, typically after user has successfully reset their password
    return render(request, 'registration/password_reset_complete.html')