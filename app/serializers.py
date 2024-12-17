from rest_framework import serializers
from app.models import *


class Employee_serializers(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'

    # eno=serializers.IntegerField()
    # ename=serializers.CharField(max_length=200)
    # esal=serializers.IntegerField()
    # eaddress=serializers.CharField(max_length=200)

    # def validate_esal(self,value):
    #     if value>5000:
    #         return value
    #     raise serializers.ValidationError("sal more then 5000")
    
    # def validate(self, data):
    #     ename=data.get('ename')
    #     esal=data.get('esal')
    #     if ename.lower()=='venkat':
    #         if esal==50000:
    #             raise serializers.ValidationError("less then 50000")
    #     return data

            
    #     return data

    # def create(self, validated_data):
    #     return Employee.objects.create(**validated_data) 
    
    # def update(self, instance, validated_data):
    #     instance.eno=validated_data.get("eno",instance.eno)
    #     instance.ename=validated_data.get("ename",instance.ename)
    #     instance.esal=validated_data.get("esal",instance.esal)
    #     instance.eaddress=validated_data.get("eaddress",instance.eaddress)
    #     instance.save()
    #     return instance