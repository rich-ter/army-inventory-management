from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("proionta", views.StockListView.as_view(), name="proionta"),
    path("new", views.StockCreateView.as_view(), name='new-stock'),
    path('proion/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('proion/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),

]