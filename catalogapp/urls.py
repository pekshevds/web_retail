from django.urls import path
from .views import index
from .views import APIBrand, APIManufacturer, APICountry, APIUnit, APICategory, APIProduct

urlpatterns = [
    path('', index, name='index-page'),
    path('api/v1/brand/',                   APIBrand.as_view()),#POST
    path('api/v1/brand/<str:pk>/',          APIBrand.as_view()),#GET end PUT
    path('api/v1/manufacturer/',            APIManufacturer.as_view()),
    path('api/v1/manufacturer/<str:pk>/',   APIManufacturer.as_view()),
    path('api/v1/country/',                 APICountry.as_view()),
    path('api/v1/country/<str:pk>/',        APICountry.as_view()),
    path('api/v1/unit/',                    APIUnit.as_view()),
    path('api/v1/unit/<str:pk>/',           APIUnit.as_view()),
    path('api/v1/category/',                APICategory.as_view()),
    path('api/v1/category/<str:pk>/',       APICategory.as_view()),
    path('api/v1/product/',                 APIProduct.as_view()),
    path('api/v1/product/<str:pk>/',        APIProduct.as_view()),
]
