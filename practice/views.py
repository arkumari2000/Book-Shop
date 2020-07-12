from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .forms import *
from .decorators import *


@decorator
def register(request):
    form = UserCreate()
    if request.method == 'POST':
        form = UserCreate(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, 'Account created successfully')
            return redirect('login')
    context = {'form': form}
    return render(request, 'practice/register.html', context)


@decorator
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username or Password Incorrect')

    context = {}
    return render(request, 'practice/login.html', context)


@login_required(login_url='login')
def logOut(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def profile(request):
    customer = request.user.customer
    form = ProfileUpdate(instance=customer)
    if request.method == 'POST':
        form = ProfileUpdate(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'practice/profile.html', context)


@login_required(login_url='login')
def user(request):
    order = request.user.customer.order_set.all()
    total_order = order.count()
    total_pending_order = order.filter(status='Pending').count()
    total_delivered_order = order.filter(status='Delivered').count()
    context = {'order': order, 'total_order': total_order, 'total_pending_order': total_pending_order,
               'total_delivered_order': total_delivered_order}
    return render(request, 'practice/user.html', context)


@login_required(login_url='login')
@admin_only
def dashboard(request):
    total_order = Order.objects.count()
    total_pending_order = Order.objects.filter(status='Pending').count()
    total_delivered_order = Order.objects.filter(status='Delivered').count()
    customer = Customer.objects.all()
    order = Order.objects.all()
    context = {'total_order': total_order, 'total_pending_order': total_pending_order,
               'total_delivered_order': total_delivered_order, 'customer': customer, 'order': order}
    return render(request, 'practice/dashboard.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def products(request):
    product = Product.objects.all()
    context = {'product': product}
    return render(request, 'practice/product.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def customer(request, pk):
    customer = Customer.objects.get(id=pk)
    order = customer.order_set.all()
    context = {'customer': customer, 'order': order}
    return render(request, 'practice/customer.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def update(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderUpdate(instance=order)
    if request.method == 'POST':
        form = OrderUpdate(request.POST, instance=order)
        if form.is_valid:
            form.save()
            return redirect('/')
    context = {'order': order, 'form': form}
    return render(request, 'practice/update.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def Delete(request, pk):
    order = Order.objects.get(id=pk)
    product = order.product.name
    if request.method == 'POST':
        order.delete()
        return redirect('/')

    context = {'product': product}
    return render(request, 'practice/delete.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def updateBook(request, pk):
    product = Product.objects.get(id=pk)
    form = BookUpdate(instance=product)
    if request.method == 'POST':
        form = BookUpdate(request.POST, instance=product)
        if form.is_valid:
            form.save()
            return redirect('products')
    context = {'product': product, 'form': form}
    return render(request, 'practice/updateBook.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def DeleteBook(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('/')

    context = {'product': product}
    return render(request, 'practice/delete.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def addproduct(request):
    form = AddBook()
    if request.method == 'POST':
        form = AddBook(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')

    context = {'form': form}
    return render(request, 'practice/addproduct.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def order(request, pk):
    customer = Customer.objects.get(id=pk)
    order_formset = inlineformset_factory(
        Customer, Order, fields=('product', 'status'), extra=5)
    formset = order_formset(queryset=Order.objects.none(), instance=customer)
    if request.method == 'POST':
        formset = order_formset(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset, 'customer': customer}
    return render(request, 'practice/order.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def newcustomer(request):
    form = NewCustomer()
    if request.method == 'POST':
        form = NewCustomer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'practice/customerform.html', context)


@login_required(login_url='login')
@allowed_user(allowed_roles=['admin'])
def DeleteCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')

    context = {'customer': customer}
    return render(request, 'practice/delete.html', context)
