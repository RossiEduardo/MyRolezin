from rest_framework import serializers
from .models import MyRolezin

class MyRolezinSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyRolezin
        fields = ('id', 'title', 'description', 'completed')