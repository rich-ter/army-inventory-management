from django.urls import path

from . import views

app_name = 'DjangoHUDApp'
urlpatterns = [
    # in use
    #general pages
    path('', views.pageLogin, name='pageLogin'),
    path('dashboard', views.index, name='index'),
    path('404/', views.error404, name='error404'),

    #product pages
    path('product', views.pageProduct, name='pageProduct'),
    path('add-product', views.add_product, name='add_product'),
    path('product-details/<int:product_id>/', views.product_details, name='pageProductDetails'),
    path('api/products/', views.ProductApiList.as_view(), name='api-products'),

    #order pages
    path('add-shipment', views.add_shipment, name='add_shipment'),
    path('add-shipment-two', views.add_shipment_two, name='add_shipment_two'),
    path('order', views.pageOrder, name='pageOrder'),
    path('order-details/<int:shipment_id>/', views.pageOrderDetails, name='pageOrderDetails'),

    #warehouse pages
    path('warehouse', views.pageWarehouse, name='pageWarehouse'),

    path('recipient', views.pageRecipient, name='pageRecipient'),


    path('page/data-management', views.pageDataManagement, name='pageDataManagement'),

    # not in use
    path('analytics/', views.analytics, name='  '),
    path('widgets/', views.widgets, name='widgets'),
    path('chart/js/', views.chartJs, name='chartJs'),
    path('chart/apex/', views.chartApex, name='chartApex'),
    path('map/', views.map, name='map'),
    path('page/search-results', views.pageSearchResults, name='pageSearchResults'),
    path('page/coming-soon', views.pageComingSoon, name='pageComingSoon'),
    path('page/error', views.pageError, name='pageError'),
    path('page/register', views.pageRegister, name='pageRegister'),
    path('page/data-management', views.pageDataManagement, name='pageDataManagement'),
    path('page/file-manager', views.pageFileManager, name='pageFileManager'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('helper/', views.helper, name='helper')
]

handler404 = 'DjangoHUDApp.views.handler404'
