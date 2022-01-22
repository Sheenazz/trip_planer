from rest_framework import serializers

from .models import Area


class AreaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'
