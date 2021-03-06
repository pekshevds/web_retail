from django.urls import path
from .views import APIBrand, APIManufacturer, APICountry, APIUnit, APICategory, APIProduct, APIOrder

urlpatterns = [    
    path('v1/brand/',                   APIBrand.as_view()),#POST
    path('v1/brand/<str:pk>/',          APIBrand.as_view()),#GET end PUT
    path('v1/manufacturer/',            APIManufacturer.as_view()),
    path('v1/manufacturer/<str:pk>/',   APIManufacturer.as_view()),
    path('v1/country/',                 APICountry.as_view()),
    path('v1/country/<str:pk>/',        APICountry.as_view()),
    path('v1/unit/',                    APIUnit.as_view()),
    path('v1/unit/<str:pk>/',           APIUnit.as_view()),
    path('v1/category/',                APICategory.as_view()),
    path('v1/category/<str:pk>/',       APICategory.as_view()),
    path('v1/product/',                 APIProduct.as_view()),
    path('v1/product/<str:pk>/',        APIProduct.as_view()),
    path('v1/order/',                   APIOrder.as_view()),
    path('v1/order/<str:pk>/',          APIOrder.as_view()),
]