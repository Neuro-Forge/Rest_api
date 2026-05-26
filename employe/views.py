from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from api.serializers import employeserializer


class EmployeForwardView(APIView):
    def get(self, request):
        # Reuse the same serializer/data as /api/employe/
        qs = models.employe.objects.all()
        serializer = employeserializer(qs, many=True)
        return Response(serializer.data)

