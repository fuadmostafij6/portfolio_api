from django.urls import path
from .views import Intro_list

urlpatterns = [
    path('intro_list/', Intro_list.as_view()),
  
    
   
]