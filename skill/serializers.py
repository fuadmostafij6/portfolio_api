from doctest import SKIP
from .models import Skill
from rest_framework import serializers

class SKillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = "__all__"
        depth = 1