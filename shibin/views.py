from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins, viewsets
from rest_framework.response import Response
from .models import shibin
from .serializers import shibinserializer
# Create your views here.

class shibin(viewsets.ViewSet):
    def list(self, request):
        queryset = shibin.objects.all()
        serializer = shibinserializer(queryset, many=True)
        return Response(serializer.data)
   
    
    
    