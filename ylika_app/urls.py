from django.urls import path
from . import views

urlpatterns = [
    #αρχική σελιδα με dashboard
    path("", views.home, name="home"),

    #σελιδες για τα προιοντα, λιστα, προσθηκη, edit, διαγραφη
    path("proionta", views.StockListView.as_view(), name="proionta"),
    path("new", views.StockCreateView.as_view(), name='new-stock'),
    path('proion/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('proion/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),

    #σελιδες για παραληπτες, λιστα, προσθηκη, edit, διαγραφη.
    path("paraliptes", views.ParaliptesListView.as_view(), name="paraliptes"),


]