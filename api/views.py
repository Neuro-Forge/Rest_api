from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import students
from .serializers import studentserializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import mixins, generics

from .serializers import employeserializer
from employe.models import employe as EmployeModel
from django.http import Http404


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'GET':
        student = students.objects.all()
        serializer = studentserializer(student, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Fetch/update/delete a particular student using their id."""
@api_view(['GET', 'PUT', 'DELETE'])
def student_views(request, id):
    try:
        student = students.objects.get(pk=id)
    except students.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = studentserializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'PUT':
        serializer = studentserializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class employe(APIView):
    def get(self, request):
        qs = EmployeModel.objects.all()
        serializer = employeserializer(qs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = employeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
class employe(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    #List/create only for EmployeModel.

    queryset = EmployeModel.objects.all()
    serializer_class = employeserializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""
"""
class employe_detail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
   queryset = EmployeModel.objects.all()
   serializer_class = employeserializer

   # Use DRF default lookup kwarg: "pk".
   def get(self, request, *args, **kwargs):
      return self.retrieve(request, *args, **kwargs)
   def put(self,request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
   def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    """
    
class employe(generics.ListAPIView,generics.CreateAPIView,generics.UpdateAPIView):
    queryset = EmployeModel.objects.all()
    serializer_class = employeserializer

class employe_detail(generics.RetrieveAPIView,generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = EmployeModel.objects.all()
    serializer_class = employeserializer
    lookup_field = 'pk'