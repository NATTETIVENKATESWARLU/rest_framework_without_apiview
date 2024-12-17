from django.shortcuts import render
from app.serializers import *
from app.models import *
from django.http import HttpResponse
from django.views import View
#---------------------------------------------------------------------------------------------------------------
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
#---------------------------------------------------------------------------------------------------------------
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import io


# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class cbv_data_json(View):

    def get(self,request,*args,**kwargs):
        json_data=request.body

        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get("id",None)
        if id is not None:
            emp=Employee.objects.get(eno=id)
            serializers=Employee_serializers(emp)
            json_data=JSONRenderer().render(serializers.data)
            return HttpResponse(json_data,content_type="application/json")
        
        qs=Employee.objects.all()
        serializers=Employee_serializers(qs,many=True)
        json_data=JSONRenderer().render(serializers.data)
        return HttpResponse(json_data,content_type="application/json")
    
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=Employee_serializers(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg={"msg":"data create successfully"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json",status=400)
    
    def put(self,request,*args,**kwargs):
        
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get("id")
        emp=Employee.objects.get(eno=id)
        serializer=Employee_serializers(emp,data=pdata,partial=True)

        if serializer.is_valid():
            serializer.save()
            msg={"msg":"record updated successfully"}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type="application/json")
        
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json",status=400)
    
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get("id")
        emp=Employee.objects.get(eno=id)
        emp.delete()
        msg={"msg":"record deleted successfully"}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type="application/json")