from rest_framework import serializers
from .models import Vape

class VapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vape
        fields = ['id','name','description']