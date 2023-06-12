from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializer import StudentSerializer
from django.http import JsonResponse
from .models import Student

# Create your views here.

@api_view(['POST'])
def register_student(request) :

    try :
        params = request.data

        serializrd_data = StudentSerializer(data = params)

        if serializrd_data.is_valid():
            serializrd_data.save()


            return JsonResponse({'status_code':201,'massage':'success'})
        else :
            return JsonResponse({'status_code':403,'massage':'form error '})
        
    except :
        return JsonResponse({'status_code':500,'massage':'something error '})
    
@api_view(['GET'])
def view_student(request):
    student = Student.objects.all()
    serialized_data = StudentSerializer(student,many = True)
    return JsonResponse({"statusc code":300,"students":serialized_data.data})

# singledata fetching

def single_data_view(requst,id):
    try :
        student = Student.objects.get(id=id)
        serialized_data = StudentSerializer(student)
        return JsonResponse({"status_code":200,"student":serialized_data.data})
    except :
        return JsonResponse({"status_code":404,"student":[],'msg':'not found'})


# updating student
@api_view(['PUT'])
def update_student(request,id):
    try :  
        params = request.data
        student = Student.objects.get(id=id)
        serialized_data = StudentSerializer(data=params,instance=student)
        if serialized_data.is_valid():
            serialized_data.save()
            return JsonResponse({"stats_code":200,'student':[],"msg":"successfull"})
        else:
            return JsonResponse({"sts_code":404,'student':[],'msg':'form not valid'})
        
    except :
        return JsonResponse({"ststus_code":404,"msg":"something went wrong"})


# deleting
@api_view(['DELETE'])
def delete(request,id):
    try :
        student = Student.objects.get(id=id).delete()
        return JsonResponse({"status code":200,"msg":"successfull"})
    except :
        return JsonResponse({"status code":200,"msg":"enterd wrong data"})