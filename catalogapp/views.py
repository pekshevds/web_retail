from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .models import Brand, Manufacturer, Country, Unit, Category, Product
from .serializers import BrandSerializer, ManufacturerSerializer, CountrySerializer, UnitSerializer, CategorySerializer, ProductSerializer

import json
# Create your views here.
def index(request):

    return render(request, 'catalog/index.html')




class APIBrand(APIView):

    def get(self, reques, id=''):
        if id == '':
            brands = Brand.objects.all()
            serialaizer = BrandSerializer(brands, many=True)
        else:
            try:
                brands = Brand.objects.get(id=id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST) 

            serialaizer = BrandSerializer(brands)
        
        return Response(serialaizer.data)

    def post(self, request):
                
        try:
            brand = Brand.objects.get(id=request.data['id'])
        except:
            brand = None

        if brand:#PUT
            serialaizer = BrandSerializer(brand, data=request.data)
        else:
            serialaizer = BrandSerializer(data=request.data)
                
        
        if serialaizer.is_valid():            
            serialaizer.save()
            return Response(serialaizer.data, status=status.HTTP_201_CREATED)

        return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIManufacturer(APIBrand):
    
    def get(self,request):
        
        manufactures = Manufacturer.objects.all()
        serialaizer = ManufacturerSerializer(manufactures, many=True)
        
        return Response(serialaizer.data)
    
    def post(self, request):
        
        serialaizer = ManufacturerSerializer(data=request.data)
        
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data, status=status.HTTP_201_CREATED)

        return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

class APICountry(APIBrand):
    
    def get(self,request):
        
        countryes = Country.objects.all()
        serialaizer = CountrySerializer(countryes, many=True)
        
        return Response(serialaizer.data)
    
    def post(self, request):
        
        serialaizer = CountrySerializer(data=request.data)
        
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data, status=status.HTTP_201_CREATED)

        return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

class APIUnit(APIBrand):
    
    def get(self,request):
        
        units = Unit.objects.all()
        serialaizer = UnitSerializer(units, many=True)
        
        return Response(serialaizer.data)

    def post(self, request):
        
        serialaizer = UnitSerializer(data=request.data)
        
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data, status=status.HTTP_201_CREATED)

        return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

class APICategory(APIBrand):
    
    def get(self,request):
        
        categoryes = Category.objects.all()
        serialaizer = CategorySerializer(categoryes, many=True)
        
        return Response(serialaizer.data)
    
    def post(self, request):
        
        serialaizer = CategorySerializer(data=request.data)
        
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data, status=status.HTTP_201_CREATED)

        return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)

class APIProduct(APIBrand):
    
    def get(self,request):
        
        products = Product.objects.all()
        serialaizer = ProductSerializer(products, many=True)
        
        return Response(serialaizer.data)
    
    def post(self, request):
        
        serialaizer = ProductSerializer(data=request.data)
        
        if serialaizer.is_valid():
            serialaizer.save()
            return Response(serialaizer.data, status=status.HTTP_201_CREATED)

        return Response(serialaizer.errors, status=status.HTTP_400_BAD_REQUEST)