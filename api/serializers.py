from rest_framework import serializers
from . models import *

class SmlrUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmlrUrl
        fields = '__all__'


class DashboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dashboard
        fields = '__all__'


class StatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stat
        fields = '__all__'

