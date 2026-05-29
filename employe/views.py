from rest_framework.response import Response
from rest_framework.views import APIView
from streamlit import status
from . import models
from api.serializers import employeserializer


class EmployeForwardView(APIView):
    def get(self, request):
        # Reuse the same serializer/data as /api/employe/
        qs = models.employe.objects.all()
        serializer = employeserializer(qs, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = employeserializer(data = request.data)
        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
