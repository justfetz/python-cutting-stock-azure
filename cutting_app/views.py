from django.shortcuts import render
from .forms import CuttingForm
from .cutting_logic import cutting_stock  # Import our cutting_stock function

def index(request):
    return render(request, 'index.html')


def cutting_view(request):
    patterns_with_waste = []

    if request.method == "POST":
        form = CuttingForm(request.POST)
        if form.is_valid():
            stock_width = form.cleaned_data['stock_width']
            orders_str = form.cleaned_data['orders']
            orders = [(int(pair.split('*')[0]), int(pair.split('*')[1])) for pair in orders_str.split(',')]
            patterns_with_waste = cutting_stock(orders, stock_width)
            
    for pattern in patterns_with_waste:
        print(pattern)
    else:
        form = CuttingForm()

    return render(request, 'input.html', {'form': form, 'patterns_with_waste': patterns_with_waste})




