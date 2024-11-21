from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Stock, Correlation, COTReport
from .forms import StockForm
from django.views.generic import ListView, CreateView
from . import cot

def home(response):
    return render(response, 'main/home.html')


# Create your views here.

class IndexView(ListView):
    model = Stock
    template_name = 'main/index.html'
    context_object_name = 'stocks'
    paginate_by = 10
# adds new stock
def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            new_stock = form.cleaned_data['name']
            t = Stock(name=new_stock)
            t.save()
            return render(request, 'main/index.html')
    else:
        form = StockForm()
    return render(request, 'main/create.html', {'form': form})
   
def view_cot(request):
    if request.method == 'POST':
        if request.POST.get('collect'):
            market_list = Stock.objects.all()
            for market in market_list:

                # https://docs.python.org/3/library/pdb.html#debugger-commands
                breakpoint()

                if   cot.data_finder(market.symbol,cot.fetch_page()) != None:
                    longs, shorts = cot.data_finder(market.symbol, cot.fetch_page())
                    cot.save_data(market.symbol, longs, shorts)
    return render(request, 'main/cot.html', {'reports': COTReport.objects.all()})
              

