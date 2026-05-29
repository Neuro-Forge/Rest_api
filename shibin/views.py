from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics, mixins, viewsets
from employe.models import employe as EmployeModel
from api.serializers import employeserializer
# Create your views here.

class shibin(viewsets.ViewSet):
    queryset = EmployeModel.objects.all()
    serializer_class = employeserializer