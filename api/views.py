from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import students
from .serializers import studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def index(request):
   if request.method == 'GET':
        student = students.objects.all()
        serializer = studentserializer(student, many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)
   
   elif request.method == 'POST':
        serializer =  studentserializer(data =request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status= status.HTTP_201_CREATED)
        
        print(serializer.errors)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

"""
now we are going the fetch the data of a particular student using his id

"""
@api_view(['GET','PUT','DELETE'])
def student_views(request,id):
   # pass
   try:
      student  = students.objects.get(pk = id)
   
   except students.DoesNotExist:
      return Response(status = status.HTTP_404_NOT_FOUND)
   
   if request.method == 'GET':
      
      serializer = studentserializer(student)
      return Response(serializer.data , status = status.HTTP_200_OK)
   
   #now  we are going to update the data of a particular student using his id
   elif request.method == 'PUT':
      serializer =studentserializer(student, data = request.data) 
      """"
      in this  part we are added the instance of the student and the data that we want to update 
      becouse we are going to update the data of a particular student using his id
      """
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status = status.HTTP_200_OK)
      else:
         return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)
      """
        now  we are learned how to update the data now we need to learn 
        how to delete the data 
        """
   elif request.method == 'DELETE':
      student.delete()
      return Response(status = status.HTTP_204_NO_CONTENT)