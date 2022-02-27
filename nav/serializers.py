from .models import Nav
from rest_framework import serializers

class NavSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nav
        fields = "__all__"
        depth = 1