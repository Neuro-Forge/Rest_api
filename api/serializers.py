from  rest_framework import serializers
from .models import students
from employe.models import employe
class studentserializer(serializers.ModelSerializer):
    class Meta:
        model =students
        fields = '__all__'

class employeserializer(serializers.ModelSerializer):
    class Meta:
        model = employe
        fields = '__all__'       