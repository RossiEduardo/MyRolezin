from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MyRolezinSerializer
from .models import MyRolezin
from rest_framework.decorators import api_view
from django.http import HttpResponse


# Create your views here.

class MyRolezinView(viewsets.ModelViewSet):
    serializer_class = MyRolezinSerializer
    queryset = MyRolezin.objects.all()




@api_view(['GET'])
def filter(request):
    return HttpResponse("oi")   