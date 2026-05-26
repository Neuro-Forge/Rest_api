from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import students
from .serializers import studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def index(request):
   if request.method == 'GET':
        student = students.objects.all()
        serializer = studentserializer(student, many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)


