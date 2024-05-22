from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.http import HttpResponse  # Add this import
from .forms import ProductForm, ShipmentForm, ShipmentItemFormSet
from .models import Product, Shipment, Warehouse, Recipient, ShipmentItem, Stock
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Sum,F, Q
from django.contrib.auth.decorators import login_required
from .filters import ProductFilter


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

def logout_view(request):
     logout(request)
     return redirect('DjangoHUDApp:pageLogin')

# Function for creating a product 
# Function for creating a product
def add_product(request):
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request:
        form = ProductForm(request.POST, request.FILES)  # Ensure that request.FILES is also passed
        if form.is_valid():
            # Save the new product to the database
            form.save()
            # Redirect to a new URL:
            return redirect('DjangoHUDApp:pageProduct')  # Redirect to an appropriate page after saving
        else:
            # If the form is not valid, render the same page with validation errors
            return render(request, 'pages/add_product.html', {
                'form': form,
                'product_category_choices': Product.PRODUCT_CATEGORY,
                'product_usage_choices': Product.PRODUCT_USAGE,
                'unit_of_measurement_choices': Product.MEASUREMENT_TYPES,
            })
    else:
        # If this is a GET (or any other method) create the default form.
        form = ProductForm()
        context = {
            'form': form,
            'product_category_choices': Product.PRODUCT_CATEGORY,
            'product_usage_choices': Product.PRODUCT_USAGE,
            'unit_of_measurement_choices': Product.MEASUREMENT_TYPES,
        }
        return render(request, 'pages/add_product.html', context)

@login_required
def pageProduct(request):
    user_groups = request.user.groups.values_list('name', flat=True)
    query = request.GET.get('q', '')  # Get the search query if it exists, otherwise default to an empty string

    if 'ΔΟΡΥΦΟΡΙΚΑ' in user_groups:
        # Filter for ΔΟΡΥΦΟΡΙΚΑ usage
        products_list = Product.objects.filter(usage='ΔΟΡΥΦΟΡΙΚΑ')
    elif 'ΔΙΔΕΣ' in user_groups:
        # Show all except ΔΟΡΥΦΟΡΙΚΑ products
        products_list = Product.objects.exclude(usage='ΔΟΡΥΦΟΡΙΚΑ')
    else:
        # Show all products to other users (adjust as necessary)
        products_list = Product.objects.all()

    if query:
        products_list = products_list.filter(Q(name__icontains=query) | Q(category__icontains=query))

    paginator = Paginator(products_list, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    context = {'products': products, 'query': query}
    return render(request, "pages/page-product.html", context)

# Function for individual product details

def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'pages/page-product-details.html', {'product': product})



# Function for creating a product 
@login_required  # Ensure that only logged-in users can access this view
def add_shipment(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST, request.FILES)
        # Ensure the prefix matches what you use in the template and is consistent
        formset = ShipmentItemFormSet(request.POST, prefix='shipmentitem')
        if form.is_valid():
            shipment = form.save(commit=False)
            shipment.user = request.user
            # Temporarily save shipment to associate it correctly with formset instances
            shipment.save()
            formset = ShipmentItemFormSet(request.POST, instance=shipment, prefix='shipmentitem')
            if formset.is_valid():
                formset.save()
                return redirect('DjangoHUDApp:pageOrder')  # Ensure this is the correct path
    else:
        form = ShipmentForm()
        formset = ShipmentItemFormSet(prefix='shipmentitem')  # Provide prefix here as well
    return render(request, 'pages/add_order.html', {'form': form, 'formset': formset})

def add_shipment_two(request):
    if request.method == 'POST':
        form = ShipmentForm(request.POST)  # Including request.FILES for completeness
        if form.is_valid():
            form.save()
            return redirect('DjangoHUDApp:pageOrder')  # Redirect as appropriate
    else:
        form = ProductForm()
        warehouses = Warehouse.objects.all()  # Fetch all warehouses

    context = {
        'form': form,
        'warehouses': warehouses,  # Pass warehouses in the context
    }
    
    return render(request, 'pages/add_order_two.html', context)

@login_required
def pageOrder(request):
    user = request.user

    # Admin users see all shipments
    if user.is_superuser:
        shipments_list = Shipment.objects.all()
    else:
        # Filter shipments by the groups of the user
        user_groups = user.groups.values_list('name', flat=True)
        if 'ΔΙΔΕΣ' in user_groups:
            # Users in ΔΙΔΕΣ see shipments from all users in this group
            shipments_list = Shipment.objects.filter(user__groups__name='ΔΙΔΕΣ')
        elif 'ΔΟΡΥΦΟΡΙΚΑ' in user_groups:
            # Users in ΔΟΡΥΦΟΡΙΚΑ only see their own shipments
            shipments_list = Shipment.objects.filter(user=user)
        else:
            # Default to no shipments if no specific group is found
            shipments_list = Shipment.objects.none()

    paginator = Paginator(shipments_list, 10)  # Show 10 products per page
    page_number = request.GET.get('page')
    shipments = paginator.get_page(page_number)

    context = {'shipments': shipments}
    return render(request, "pages/page-order.html", context)

@login_required
def pageWarehouse(request):
    # Get the user's groups as a list of strings
    user_groups = request.user.groups.values_list('name', flat=True)

    # Initialize an empty queryset
    warehouses_list = Warehouse.objects.none()

    # Check if user is a superuser or in the Admin group
    if request.user.is_superuser or 'Admin' in user_groups:
        # Show all warehouses if user is an admin or in the admin group
        warehouses_list = Warehouse.objects.annotate(total_stock=Sum('stocks__quantity'))

    # Check for 'Doriforika' group and filter accordingly
    elif 'ΔΟΡΥΦΟΡΙΚΑ' in user_groups:
        # Filter warehouses to show only those related to "Doriforika"
        warehouses_list = Warehouse.objects.filter(name="Δορυφορικα").annotate(
            total_stock=Sum('stocks__quantity')
        )

    # Check for 'ΔΙΔΕΣ' group and filter for "KEPIK" and "TAGMA" warehouses
    elif 'ΔΙΔΕΣ' in user_groups:
        # Filter warehouses to show only "KEPIK" and "TAGMA"
        warehouses_list = Warehouse.objects.filter(name__in=["ΚΕΠΙΚ", "ΤΑΓΜΑ"]).annotate(
            total_stock=Sum('stocks__quantity')
        )

    context = {'warehouses': warehouses_list}
    return render(request, "pages/page-warehouse.html", context)

@login_required
def pageDataManagement(request):
    user = request.user
    products = Product.objects.none()  # Start with no products
    warehouse_filter = []  # List to hold filtered warehouse names

    if user.is_superuser:
        products = Product.objects.annotate(total_stock=Sum('stocks__quantity'))
        warehouse_filter = ['ΚΕΠΙΚ', 'ΔΟΡΥΦΟΡΙΚΑ', 'ΤΑΓΜΑ']
    else:
        user_groups = user.groups.values_list('name', flat=True)
        if 'ΔΙΔΕΣ' in user_groups:
            products = Product.objects.exclude(usage='ΔΟΡΥΦΟΡΙΚΑ').annotate(total_stock=Sum('stocks__quantity'))
            warehouse_filter = ['ΚΕΠΙΚ', 'ΤΑΓΜΑ']  # Excludes ΔΟΡΥΦΟΡΙΚΑ warehouse
        elif 'ΔΟΡΥΦΟΡΙΚΑ' in user_groups:
            products = Product.objects.filter(usage='ΔΟΡΥΦΟΡΙΚΑ').annotate(total_stock=Sum('stocks__quantity'))
            warehouse_filter = ['ΔΟΡΥΦΟΡΙΚΑ']  # Only ΔΟΡΥΦΟΡΙΚΑ warehouse

    # Fetching warehouses once based on required filters
    warehouses = Warehouse.objects.filter(name__in=warehouse_filter)
    warehouse_dict = {wh.name: wh for wh in warehouses}

    # Annotating stock information from the filtered warehouses
    for product in products:
        product.stock_kepik = product.stock_doriforika = product.stock_tagma = 0
        stocks = Stock.objects.filter(product=product, warehouse__in=warehouses)
        for stock in stocks:
            if stock.warehouse.name == 'ΚΕΠΙΚ':
                product.stock_kepik = stock.quantity
            elif stock.warehouse.name == 'ΔΟΡΥΦΟΡΙΚΑ':
                product.stock_doriforika = stock.quantity
            elif stock.warehouse.name == 'ΤΑΓΜΑ':
                product.stock_tagma = stock.quantity

    context = {
        'appContentFullHeight': 1,
        'appContentClass': 'py-3',
        'products_with_stock': products,
        # Including warehouse access flags for template rendering
        'can_view_kepik': 'ΚΕΠΙΚ' in warehouse_filter,
        'can_view_doriforika': 'ΔΟΡΥΦΟΡΙΚΑ' in warehouse_filter,
        'can_view_tagma': 'ΤΑΓΜΑ' in warehouse_filter,
    }

    return render(request, 'pages/page-data-management.html', context)

def stockPerWarehouse(request, warehouse_id):
    # Get the specific warehouse
    warehouse = get_object_or_404(Warehouse, pk=warehouse_id)
    
    # Get the stock items that belong to this warehouse
    # Assuming you have a reverse relationship from Warehouse to Stock set up in your models
    # If not, adjust the following query to match your model relationships
    stock_items = Stock.objects.filter(warehouse=warehouse).select_related('product')

    # Include both the warehouse and the stock items in the context
    context = {
        'warehouse': warehouse,
        'stock_items': stock_items
    }
    
    return render(request, "pages/page-stock-per-warehouse.html", context)


def pageRecipient(request):
    recipients_list = Recipient.objects.all()
    context = {'recipients': recipients_list}
    return render(request, "pages/page-recipient.html", context)


def index(request):
	return render(request, "pages/index.html")



# def product_details(request, product_id):
#     product = get_object_or_404(Product, pk=product_id)
#     return render(request, 'pages/page-product-details.html', {'product': product})




def pageOrderDetails(request, shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    shipment_items = ShipmentItem.objects.filter(shipment=shipment)
    return render(request, "pages/page-order-details.html", {"shipment": shipment, "shipment_items": shipment_items})


# def pageOrderDetails(request, shipment_id):  # Accept shipment_id as a parameter
#     shipment = get_object_or_404(Shipment, pk=shipment_id)
#     # shipment_items = ShipmentItem.objects.filter(shipment=shipment)
#     return render(request, "pages/page-order-details.html", {'shipment': shipment})



def order_print(request,shipment_id):
    shipment = get_object_or_404(Shipment, pk=shipment_id)
    shipment_items = ShipmentItem.objects.filter(shipment=shipment)
    return render(request, "doriforika-protokolo.html", {"shipment": shipment, "shipment_items": shipment_items})








# # # # # # # # # # # # ANALYTICS PAGES # # # # # # # # # # # # 

def analytics(request):
	return render(request, "pages/analytics.html")


def chartJs(request):
	return render(request, "pages/chart-js.html")

def chartApex(request):
	return render(request, "pages/chart-apex.html")



# # # # # # # # # # # # 404 PAGES # # # # # # # # # # # # 


def pageError(request):
	context = {
		"appSidebarHide": 1,
		"appHeaderHide": 1,
		"appContentClass": 'p-0'
	}
	return render(request, "pages/page-error.html", context)

	
def error404(request):
	context = {
		"appSidebarHide": 1,
		"appHeaderHide": 1,
		"appContentClass": 'p-0'
	}
	return render(request, "pages/page-error.html", context)

def handler404(request, exception = None):
	return redirect('/404/')

def handler404(request, exception):
    context = {} # Add any context variables if needed
    return render(request, 'pages/page-error.html', context, status=404)