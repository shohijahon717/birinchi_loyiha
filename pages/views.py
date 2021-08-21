from django.shortcuts import render
from django.views.generic import TemplateView  # HTML ni ekranga chiqarish uchun 


# Create your views here.

class HomePagesView(TemplateView):
    template_name = 'home.html'   # qaysi html ni ekranga chiqarish