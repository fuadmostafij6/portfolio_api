from django.urls import path
from .views import *

urlpatterns = [
    path('portfolio_list/', Portfolio_list.as_view()),
  
    
   
]