from django.shortcuts import render
from django.http import HttpResponse
from app.models import Car
from django.template import loader
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from app.forms import CarForm

from django.views.generic import ListView




PARAMS = ['manufacturer', 'model', 'year', 'transmission', 'color']

class CarList(ListView):
    model = Car
    template_name = 'index.html'
    form_class = CarForm


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cars'] = self.get_queryset()
        context['form'] = self.form_class
        return context


    def get_queryset(self):
        qs = self.model.objects.all()
        manufacturer = self.request.GET.get('manufacturer')
        model = self.request.GET.get('model')
        year = self.request.GET.get('year')
        transmission = self.request.GET.get('transmission')
        color = self.request.GET.get('color')
        if manufacturer:
            qs = qs.filter(manufacturer=manufacturer)
        if model:
            qs = qs.filter(model=model)
        if year:
            qs = qs.filter(year=year)
        if transmission:
            qs = qs.filter(transmission=transmission)
        if color:
            qs = qs.filter(color=color)
        return qs


# def index(request):
#     template = loader.get_template('index.html')
#     success_url = reverse_lazy('index')
#     form = CarForm(request.GET)
#     print(request.GET['manufacturer'])
    
#     cars = Car.objects.all()
#     # if params:
#     #     for param in params.items():
#     #         cars = cars.filter(param)
#     context = {
#         'cars': cars,
#         'form': form,
#     }
#     return HttpResponse(template.render(context, request))
    

# def check_params(data):
#     check = False
#     for param in PARAMS:
#         if param in data:
#             check = True
#     return check
