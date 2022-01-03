from django.urls import path
from .views import index
from .views import APIBrand, APIManufacturer, APICountry, APIUnit, APICategory, APIProduct

urlpatterns = [
    path('', index, name='index-page'),
    path('api/v1/brand/',           APIBrand.as_view()),
    path('api/v1/brand/<str:id>/',  APIBrand.as_view()),
    path('api/v1/manufacturer/',    APIManufacturer.as_view()),
    path('api/v1/country/',         APICountry.as_view()),
    path('api/v1/unit/',            APIUnit.as_view()),
    path('api/v1/category/',        APICategory.as_view()),
    path('api/v1/product/',         APIProduct.as_view()),
]
