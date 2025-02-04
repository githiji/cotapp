from django.shortcuts import render,get_object_or_404
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
            
            t = Stock(symbol=new_stock)
            t.save()
            return HttpResponseRedirect('/index/')
    else:
        form = StockForm()
    return render(request, 'main/create.html', {'form': form})
   
def view_cot(request):
    if request.method == 'POST':
        if request.POST.get('collect'):
            market_list = Stock.objects.all()
            for market in market_list:
                # https://docs.python.org/3/library/pdb.html#debugger-commands
                if   cot.data_finder(market.symbol,cot.fetch_page()) != None or []:
                    longs, shorts = cot.data_finder(market.symbol, cot.fetch_page())
                    cot.save_data(market.symbol, longs, shorts)
                else:
                    return HttpResponse("some data in your database has error")
    return render(request, 'main/cot.html', {'reports': COTReport.objects.all()})

def symbol(request, id):
    stock = get_object_or_404(Stock, id=id)
    return render(request,'main/symbol.html' , {'stock':stock})
              

