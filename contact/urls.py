from django.urls import path
from .views import ContactView

urlpatterns = [
 
    path('contact_list/', ContactView),
    
   
]