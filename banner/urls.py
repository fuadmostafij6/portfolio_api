from django.urls import path
from .views import banner_list,brand_list

urlpatterns = [
    path('banner/', banner_list.as_view()),
    path('brand/', brand_list.as_view()),
    
   
]