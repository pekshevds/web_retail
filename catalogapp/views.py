from typing import List
from django.db.models.base import Model
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import serializers
from django.db import models

from .models import Brand, Manufacturer, Country, Unit, Category, Product
from .serializers import BrandSerializer, ManufacturerSerializer, CountrySerializer, UnitSerializer, CategorySerializer, ProductSerializer

# Create your views here.
def index(request):

    return render(request, 'catalog/index.html')


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