from .models import Portfolio
from .serializers import PortfolioSerializer

from rest_framework import generics,mixins

class Portfolio_list(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Portfolio.objects.all().order_by("id")
    serializer_class=PortfolioSerializer
    lookup_field = "id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)