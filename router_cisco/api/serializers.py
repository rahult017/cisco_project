from .models import *
from rest_framework import serializers


class RouterSerializer(serializers.ModelSerializer):
    class Meta:
         model = Router_Details
         fields = '__all__'
