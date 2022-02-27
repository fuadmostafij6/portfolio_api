from .models import Brand,Banner
from .serializers import BrandSerializer, BannerSerializer

from rest_framework import generics,mixins

class banner_list(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Banner.objects.all().order_by("id")
    serializer_class=BannerSerializer
    lookup_field = "id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        
class brand_list(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Brand.objects.all()
    serializer_class=BrandSerializer
    lookup_field = "id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
        
