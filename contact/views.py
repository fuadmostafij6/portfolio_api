from django.shortcuts import render
from .serializers import ContactSerializer

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def ContactView(request):
    serilizer = ContactSerializer(data=request.data)
    if serilizer.is_valid():
        serilizer.save()
    return Response({"message": "Hello, world!"})