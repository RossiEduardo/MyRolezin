from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MyRolezinSerializer
from .models import MyRolezin

# Create your views here.

class MyRolezinView(viewsets.ModelViewSet):
    serializer_class = MyRolezinSerializer
    queryset = MyRolezin.objects.all()