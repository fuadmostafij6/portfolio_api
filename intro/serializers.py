from rest_framework import serializers
from .models import Intro
class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = '__all__'
        depth = 1
        

