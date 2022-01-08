from typing import List

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from rest_framework import serializers
from django.db import models


from catalogapp.models import Brand, Category, Country, Manufacturer, Product, Unit
from catalogapp.serializers import BrandSerializer, ManufacturerSerializer, CountrySerializer, \
    UnitSerializer, CategorySerializer, ProductSerializer


from orderapp.models import Order
from orderapp.serializers import OrderSerializer
# Create your views here.

#REST classes
class APIModel(APIView):
    model = models.Model
    serializer = serializers.ModelSerializer

    def get(self, request, pk = ''):
        
        many = False
        if pk == '':
            item = self.model.objects.all()            
            many = True
        else:
            try:
                item = self.model.objects.get(pk=pk)
            except self.model.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer(item, many=many)
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

class APIOrder(APIModel):
    model = Order
    serializer = OrderSerializer