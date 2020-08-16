from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from django.views.generic.base import View
from .models import Teapack

class ShopList(View):
    def get(self, request):
        content = Teapack.objects.all()
        return render(request, 'teashop/shop-list.html', {'content': content})


# class ShopList(ListView):
#     model = Teapack
#
#     template_name = 'teashop/shop-list.html'
