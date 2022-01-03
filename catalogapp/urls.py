from django.urls import path
from .views import index
from .views import APIBrand, APIManufacturer, APICountry, APIUnit, APICategory, APIProduct
from .views import CountryGenerator

urlpatterns = [
    path('', index, name='index-page'),
    path('api/v1/brand/',                   APIBrand.as_view()),
    path('api/v1/brand/<str:id>/',          APIBrand.as_view()),
    path('api/v1/manufacturer/',            APIManufacturer.as_view()),
    path('api/v1/manufacturer/<str:id>/',   APIManufacturer.as_view()),
    path('api/v1/country/',                 APICountry.as_view()),
    path('api/v1/countryes/',               CountryGenerator.as_view()),
    path('api/v1/country/<str:id>/',        APICountry.as_view()),
    path('api/v1/unit/',                    APIUnit.as_view()),
    path('api/v1/unit/<str:id>/',           APIUnit.as_view()),
    path('api/v1/category/',                APICategory.as_view()),
    path('api/v1/category/<str:id>/',       APICategory.as_view()),
    path('api/v1/product/',                 APIProduct.as_view()),
    path('api/v1/product/<str:id>/',        APIProduct.as_view()),
]
