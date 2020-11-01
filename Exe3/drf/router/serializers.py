from rest_framework import serializers
from .models import RouterInfo


class RouterSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouterInfo
        fields = ['sapid', 'hostname', 'loopback', 'mac_address']


class RouterDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouterInfo
        fields = ['id', 'sapid', 'hostname', 'loopback', 'mac_address']