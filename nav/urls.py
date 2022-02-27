from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import NavList

urlpatterns = [
    path('navlist/', NavList.as_view()),
   
]

urlpatterns = format_suffix_patterns(urlpatterns)