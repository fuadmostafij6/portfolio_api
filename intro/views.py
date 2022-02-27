from .models import Intro
from .serializers import IntroSerializer

from rest_framework import generics,mixins

class Intro_list(generics.GenericAPIView,mixins.ListModelMixin,mixins.RetrieveModelMixin):
    queryset = Intro.objects.all().order_by("id")
    serializer_class=IntroSerializer
    lookup_field = "id"

    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)