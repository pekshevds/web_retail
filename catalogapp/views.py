from typing import List
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import serializers
from django.db import models

from .models import Brand, Manufacturer, Country, Unit, Category, Product
from .serializers import BrandSerializer, ManufacturerSerializer, CountrySerializer, UnitSerializer, CategorySerializer, ProductSerializer

from django.core.paginator import Paginator

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# Create your views here.


#Class-based views
class ProductListView(ListView):
    template_name = 'catalogapp/list.html'
    model = Product
    paginate_by = 24

    def get_queryset(self):
        return self.model.objects.all()[:100]
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        return context

class ProductDetailView(DetailView):
    template_name = 'catalogapp/item.html'
    model = Product



#Function-based views
def show_list(request):
    items = Product.objects.all()[:100]

    paginator = Paginator(items, 24)

    page_num = 1
    if 'page' in request.GET:
        page_num = request.GET['page']
    
    page = paginator.get_page(page_num)
    
    context = {
        'page_obj': page,
        }

    return render(request, 'catalogapp/list.html', context=context)

def show_item(request, pk):
    item = Product.objects.get(pk=pk)

    context = {
        'object': item,
        }

    return render(request, 'catalogapp/item.html', context=context)




#REST classes
class APIModel(APIView):
    model = models.Model
    serializer = serializers.ModelSerializer

    def get(self, request, pk):
        
        try:
            item = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer(item)
        return Response(serializer.data)

    def put(self, request, pk):
                
        try:
            item = self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            serializer = self.serializer(data=request.data)
        else:
            serializer = self.serializer(item, data=request.data)
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def post(self, request):
                
        serializer = self.serializer(data=request.data, many=isinstance(request.data, List))
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request):

        result = True    
        try:
            self.model.objects.all().delete()
        except:
            result = False
        
        if result:            
            return Response(status=status.HTTP_200_OK)

        return Response(exception=True, status=status.HTTP_400_BAD_REQUEST)

class APIBrand(APIModel):
    model = Brand
    serializer = BrandSerializer

class APIManufacturer(APIModel):
    model = Manufacturer
    serializer = ManufacturerSerializer

class APICountry(APIModel):
    model = Country
    serializer = CountrySerializer
    
class APIUnit(APIModel):
    model = Unit
    serializer = UnitSerializer
    
class APICategory(APIModel):
    model = Category
    serializer = CategorySerializer    

class APIProduct(APIModel):
    model = Product
    serializer = ProductSerializer