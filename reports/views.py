from django.shortcuts import render
from django.views.generic import (
    CreateView
)
from .models import Raportet
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, 'reports/index.html')

def support(request):
    return render(request, 'reports/support.html')

def contact(request):
    return render(request, 'reports/contact.html')

def about(request):
    return render(request, 'reports/about.html')

class RaportetCreateView(CreateView): 
    model = Raportet
    fields = ['platform', 'person_name', 'contact', 'description']
    success_url = reverse_lazy('wwwsafe-home')