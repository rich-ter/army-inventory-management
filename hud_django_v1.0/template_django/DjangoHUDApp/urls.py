from django.urls import path

from . import views

app_name = 'DjangoHUDApp'
urlpatterns = [
    # in use
    #general pages
    path('', views.pageLogin, name='pageLogin'),
    path('dashboard', views.index, name='index'),
    path('404/', views.error404, name='error404'),
    path('order', views.pageOrder, name='pageOrder'),
    path('order-details', views.pageOrderDetails, name='pageOrderDetails'),

    #product pages
    path('product', views.pageProduct, name='pageProduct'),
    path('product-details', views.pageProductDetails, name='pageProductDetails'),
    path('add-product', views.add_product, name='add_product'),

    #order pages



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