from  rest_framework import serializers
from .models import shibin

class shibinserializer(serializers.ModelSerializer):
    class Meta:
        model = shibin
        fields = '__all__'
        