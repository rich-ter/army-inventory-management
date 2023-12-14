from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("proionta", views.StockListView.as_view(), name="proionta"),
]