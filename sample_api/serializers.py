from rest_framework import serializers
from .models import *

class User_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user
        fields = ('id', 'name', 'email', 'age')
        
class Employee_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = employee
        fields = ('id', 'name', 'email', 'age')