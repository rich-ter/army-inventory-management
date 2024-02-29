from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.http import HttpResponse  # Add this import
from .forms import ProductForm, ShipmentForm
from .models import Product, Shipment, Warehouse,Recipient
from django.core.paginator import Paginator

# Function for loging a user 
def pageLogin(request):
    if request.method == 'GET':
        form = LoginForm()
    else:  # POST request
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('DjangoHUDApp:index')  # Make sure 'dashboard' is a valid named route in your urls.py
            else:
                # For debugging: Return a simple response indicating failure
                return HttpResponse("Invalid login attempt", status=401)
        else:
            # For debugging: Indicate form is not valid
            return HttpResponse("Form is not valid", status=400)
    
    context = {
        "form": form,
        "appSidebarHide": 1,
        "appHeaderHide": 1,
        "appContentClass": 'p-0'
    }
    return render(request, "pages/page-login.html", context)

# Function for creating a product 
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # Including request.FILES for completeness
        if form.is_valid():
            form.save()
            return redirect('DjangoHUDApp:pageProduct')  # Redirect as appropriate
    else:
        form = ProductForm()
    context = {
        'form': form,
        'product_category_choices': Product.PRODUCT_CATEGORY,
        'product_usage_choices': Product.PRODUCT_USAGE,
    }
    return render(request, 'pages/add_product.html', context) 

# All products page
def pageProduct(request):
    products_list = Product.objects.all()  # Query all products
    paginator = Paginator(products_list, 10)  # Show 10 products per page

    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {'products': products}
    return render(request, "pages/page-product.html", context)

# Function for individual product details

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pages/page-product-details.html', {'product': product})

# Function for creating a product 
def add_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)  # Including request.FILES for completeness
        if form.is_valid():
            form.save()
            return redirect('DjangoHUDApp:pageOrder')  # Redirect as appropriate
    else:
        form = ProductForm()
    context = {
        'form': form,
        # 'product_category_choices': Product.PRODUCT_CATEGORY,
        # 'product_usage_choices': Product.PRODUCT_USAGE,
    }
    return render(request, 'pages/add_order.html', context) 

# Function for creating a product 
def add_shipment_two(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)  # Including request.FILES for completeness
        if form.is_valid():
            form.save()
            return redirect('DjangoHUDApp:pageOrder')  # Redirect as appropriate
    else:
        form = ProductForm()
    context = {
        'form': form,
        # 'product_category_choices': Product.PRODUCT_CATEGORY,
        # 'product_usage_choices': Product.PRODUCT_USAGE,
    }
    return render(request, 'pages/add_order_two.html', context) 



# All orders page
def pageOrder(request):
    shipments_list = Shipment.objects.all()

    for shipment in shipments_list:
        shipment.products_count = shipment.shipment_items.count()

    context = {'shipments': shipments_list}
    return render(request, "pages/page-order.html", context)




def pageWarehouse(request):
    warehouses_list = Warehouse.objects.all()
    context = {'warehouses': warehouses_list}
    return render(request, "pages/page-warehouse.html", context)

def pageRecipient(request):
    recipients_list = Recipient.objects.all()
    context = {'recipients': recipients_list}
    return render(request, "pages/page-recipient.html", context)


def index(request):
	return render(request, "pages/index.html")




def pageOrderDetails(request):
	return render(request, "pages/page-order-details.html")



# # # # # # # # # # # # NOT USED # # # # # # # # # # # # 

def analytics(request):
	return render(request, "pages/analytics.html")

def widgets(request):
	return render(request, "pages/widgets.html")

def chartJs(request):
	return render(request, "pages/chart-js.html")

def chartApex(request):
	return render(request, "pages/chart-apex.html")

def map(request):
	return render(request, "pages/map.html")





def pageSearchResults(request):
	return render(request, "pages/page-search-results.html")

def pageComingSoon(request):
	context = {
		"appSidebarHide": 1,
		"appHeaderHide": 1,
		"appContentClass": 'p-0'
	}
	return render(request, "pages/page-coming-soon.html", context)

def pageError(request):
	context = {
		"appSidebarHide": 1,
		"appHeaderHide": 1,
		"appContentClass": 'p-0'
	}
	return render(request, "pages/page-error.html", context)

def pageRegister(request):
	context = {
		"appSidebarHide": 1,
		"appHeaderHide": 1,
		"appContentClass": 'p-0'
	}
	return render(request, "pages/page-register.html", context)

def pageDataManagement(request):
	context = {
		"appContentFullHeight": 1,
		"appContentClass": 'py-3'
	}
	return render(request, "pages/page-data-management.html", context)

def pageFileManager(request):
	context = {
		"appContentFullHeight": 1,
		"appContentClass": 'd-flex flex-column'
	}
	return render(request, "pages/page-file-manager.html", context)

def profile(request):
	return render(request, "pages/profile.html")


def settings(request):
	return render(request, "pages/settings.html")

def helper(request):
	return render(request, "pages/helper.html")
	
def error404(request):
	context = {
		"appSidebarHide": 1,
		"appHeaderHide": 1,
		"appContentClass": 'p-0'
	}
	return render(request, "pages/page-error.html", context)

def handler404(request, exception = None):
	return redirect('/404/')