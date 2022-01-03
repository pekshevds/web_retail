from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import generics

from .models import Brand, Manufacturer, Country, Unit, Category, Product
from .serializers import BrandSerializer, ManufacturerSerializer, CountrySerializer, UnitSerializer, CategorySerializer, ProductSerializer

import json
# Create your views here.
def index(request):

    return render(request, 'catalog/index.html')




class APIBrand(APIView):

    def get(self, request, id=''):
        if id == '':
            items = Brand.objects.all()
            if len(items)> 0:
                serializer = BrandSerializer(items, many=True)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                items = Brand.objects.get(id=id)
            except Brand.DoesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST) 

            serializer = BrandSerializer(items)
        
        return Response(serializer.data)

    def post(self, request):
                
        try:
            item = Brand.objects.get(id=request.data['id'])
        except:
            item = None

        if item:#PUT
            serializer = BrandSerializer(item, data=request.data)
        else:
            serializer = BrandSerializer(data=request.data)
                
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIManufacturer(APIView):
    
    def get(self, request, id=''):
        if id == '':
            items = Manufacturer.objects.all()
            if len(items)> 0:
                serializer = ManufacturerSerializer(items, many=True)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                items = Manufacturer.objects.get(id=id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST) 

            serializer = ManufacturerSerializer(items)
        
        return Response(serializer.data)

    def post(self, request):
                
        try:
            item = Manufacturer.objects.get(id=request.data['id'])
        except:
            item = None

        if item:#PUT
            serializer = ManufacturerSerializer(item, data=request.data)
        else:
            serializer = ManufacturerSerializer(data=request.data)
                
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APICountry(APIView):
    
    def get(self, request, id=''):
        if id == '':
            items = Country.objects.all()
            if len(items)> 0:
                serializer = CountrySerializer(items, many=True)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                items = Country.objects.get(id=id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST) 

            serializer = CountrySerializer(items)
        
        return Response(serializer.data)

    def post(self, request):
                
        try:
            item = Country.objects.get(id=request.data['id'])
        except:
            item = None

        if item:#PUT
            serializer = CountrySerializer(item, data=request.data)
        else:
            serializer = CountrySerializer(data=request.data)
                
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CountryGenerator(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class= CountrySerializer

    def post(self, request, format='json'):
        serializer= CountrySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, format='json'):
        serializer= CountrySerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)


class APIUnit(APIView):
    
    def get(self, request, id=''):
        if id == '':
            items = Unit.objects.all()
            if len(items)> 0:
                serializer = UnitSerializer(items, many=True)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                items = Unit.objects.get(id=id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST) 

            serializer = UnitSerializer(items)
        
        return Response(serializer.data)

    def post(self, request):
                
        try:
            item = Unit.objects.get(id=request.data['id'])
        except:
            item = None

        if item:#PUT
            serializer = UnitSerializer(item, data=request.data)
        else:
            serializer = UnitSerializer(data=request.data)
                
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APICategory(APIView):
    
    def get(self, request, id=''):
        if id == '':
            items = Category.objects.all()
            if len(items)> 0:
                serializer = CategorySerializer(items, many=True)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                items = Category.objects.get(id=id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST) 

            serializer = CategorySerializer(items)
        
        return Response(serializer.data)

    def post(self, request):
                
        try:
            item = Category.objects.get(id=request.data['id'])
        except:
            item = None

        if item:#PUT
            serializer = CategorySerializer(item, data=request.data)
        else:
            serializer = CategorySerializer(data=request.data)
                
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class APIProduct(APIView):
    
    def get(self, request, id=''):
        if id == '':
            items = Product.objects.all()
            if len(items)> 0:
                serializer = ProductSerializer(items, many=True)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                items = Product.objects.get(id=id)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST) 

            serializer = ProductSerializer(items)
        
        return Response(serializer.data)

    def post(self, request):
                
        try:
            item = Product.objects.get(id=request.data['id'])
        except:
            item = None

        if item:#PUT
            serializer = ProductSerializer(item, data=request.data)
        else:
            serializer = ProductSerializer(data=request.data)
                
        
        if serializer.is_valid():            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)