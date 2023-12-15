
from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, UpdateView,TemplateView
from .models import (
    Proion,
    Apothema,
    Paraliptis
)
from .filters import StockFilter
from django_filters.views import FilterView 
from .forms import StockForm
from django.contrib.messages.views import SuccessMessageMixin


class HomeView(View):
    template_name = "home.html"
    def get(self, request):        
        labels = []
        data = []        
        proion = Proion.objects.filter(is_deleted=False).order_by('-quantity')
        for item in stockqueryset:
            labels.append(item.name)
            data.append(item.quantity)
#         sales = SaleBill.objects.order_by('-time')[:3]
#         purchases = PurchaseBill.objects.order_by('-time')[:3]
        context = {
            'labels'    : labels,
            'data'      : data,
#             'sales'     : sales,
#             'purchases' : purchases
        }
        return render(request, self.template_name, context)

# VIEWS FOR THE YLIKA APP 

def home(request):
    return render(request, 'ylika_app/home.html')

# TO VIEW ΤΟ ΟΠΟΙΟ ΔΕΙΧΝΕΙ ΟΛΑ ΤA ΜΟΝΤΕΛΑ ΣΤΟ URL YLIKA_APP/PROIONTA

class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Proion.objects.all()
    template_name = 'ylika_app/proionta/proionta.html'
    paginate_by = 10 


# TO VIEW ΤΟ ΟΠΟΙΟ ΔΗΜΙΟΥΡΓΕΙ ΕΝΑ ΑΝΤΙΚΕΙΜΕΝΟ ΚΑΙ ΤΟ ΑΠΟΘΗΚΕΥΕΙ ΣΑΝ ΠΡΟΙΟΝ

class StockCreateView(SuccessMessageMixin, CreateView):
    model = Proion
    form_class = StockForm
    template_name = "ylika_app/proionta/edit_stock.html"
    success_url = 'proionta'
    success_message = "Stock has been created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'ΚΑΙΝΟΥΡΓΙΟ ΠΡΟΙΟΝ'
        context["savebtn"] = 'Προσθήκη Προιόντος'
        return context 


class StockUpdateView(SuccessMessageMixin, UpdateView):
    model = Proion
    form_class = StockForm
    template_name = "ylika_app/proionta/edit_stock.html"
    success_url = 'proionta'
    success_message = "Stock has been updated successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Stock'
        context["savebtn"] = 'Update Stock'
        context["delbtn"] = 'Delete Stock'
        return context

class StockDeleteView(View):                                                            # view class to delete stock
    template_name = "ylika_app/proionta/delete_stock.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Stock has been deleted successfully"                             # displays message when form is submitted
    
    def get(self, request, pk):
        stock = get_object_or_404(Proion, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):  
        stock = get_object_or_404(Proion, pk=pk)
        stock.is_deleted = True
        stock.save()                                               
        messages.success(request, self.success_message)
        return redirect('proionta')



class ParaliptesListView(FilterView):
    filterset_class = StockFilter
    queryset = Paraliptis.objects.all()
    template_name = 'ylika_app/paraliptes/paraliptes.html'
    paginate_by = 50 
