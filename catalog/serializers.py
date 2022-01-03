from rest_framework import fields, serializers
from .models import Brand, Country, Unit, Manufacturer, Category, Product

class BrandSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brand
        fields = ('__all__')

class ManufacturerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manufacturer
        fields = ('__all__')

class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ('__all__')

class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Unit
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product        
        fields = ('__all__')
