
from django.db import models
from django.db.models import Sum

from django.http import HttpResponse, request
from django.shortcuts import render, get_object_or_404
from django.views.generic import View, CreateView, UpdateView,TemplateView
from .models import (Proion, Apothema, Paraliptis, Apothiki )
from .filters import StockFilter
from django_filters.views import FilterView 
from .forms import StockForm, ApothemaForm
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



################# PRODUCT CRUD OPERATIONS #######################


# TO VIEW ΤΟ ΟΠΟΙΟ ΔΕΙΧΝΕΙ ΟΛΑ ΤA ΜΟΝΤΕΛΑ ΣΤΟ URL /YLIKA_APP/PROIONTA

class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Proion.objects.all()
    template_name = 'ylika_app/proionta/proionta.html'
    paginate_by = 10 

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

################# APOTHEMA CRUD OPERATIONS #######################
class ApothemaListView(FilterView):
    model = Apothema
    # queryset = Apothema.objects.all()
    template_name = 'ylika_app/apothemata/apothemata.html'
    paginate_by = 10 
    context_object_name = 'object_list'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Fetch Apothiki IDs (assuming you know these IDs)
        apothiki_ids = [1, 2, 3]  # Replace with actual IDs

        # Dictionary to hold total posotita per Proion for each Apothiki
        totals_per_apothiki = {apothiki_id: {} for apothiki_id in apothiki_ids}

        for apothiki_id in apothiki_ids:
            totals = Apothema.objects.filter(apothiki_id=apothiki_id).values('proion').annotate(
                total=Sum('posotita')).order_by('proion')

            for total in totals:
                totals_per_apothiki[apothiki_id][total['proion']] = total['total']

        context['totals_per_apothiki'] = totals_per_apothiki
        return context


class ApothemaCreateView(SuccessMessageMixin, CreateView):
    model = Apothema
    form_class = ApothemaForm
    template_name = "ylika_app/apothemata/edit_apothema.html"
    success_url = 'apothemata'
    success_message = "Apothema has been created successfully"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'ΚΑΙΝΟΥΡΓΙΟ ΑΠΟΘΕΜΑ'
        context["savebtn"] = 'Προσθήκη Αποθέματος'
        return context 


################# APOTHIKES CRUD OPERATIONS #######################
class ApothikesListView(FilterView):
    model = Apothiki
    queryset = Apothiki.objects.all()
    template_name = 'ylika_app/apothikes/apothikes.html'
    paginate_by = 10 

################# PARALIPTES CRUD OPERATIONS #######################

class ParaliptesListView(FilterView):
    filterset_class = StockFilter
    queryset = Paraliptis.objects.all()
    template_name = 'ylika_app/paraliptes/paraliptes.html'
    paginate_by = 50 


