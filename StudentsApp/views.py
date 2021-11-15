from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from StudentsApp.models import Classes,Students
from StudentsApp.serializers import ClassesSerializer,StudentsSerializer

from django.core.files.storage import default_storage

# Create your views here.
@csrf_exempt
def classesApi(request, id=0):
    if request.method=='GET':
        classes = Classes.objects.all()
        classes_serializer = ClassesSerializer(classes, many=True)
        return JsonResponse(classes_serializer.data, safe=False)
    elif request.method=='POST':
        classes_data = JSONParser().parse(request)
        classes_serializer=ClassesSerializer(data=classes_data)
        if classes_serializer.is_valid():
            classes_serializer.save()
            return JsonResponse('Class Added Successfully!', safe=False)
        return JsonResponse('Failed to Add Class', safe=False)
    elif request.method=='PUT':
        classes_data = JSONParser().parse(request)
        classes = Classes.objects.get(ClassId=classes_data['ClassId'])
        classes_serializer = ClassesSerializer(classes, data= classes_data)
        if classes_serializer.is_valid():
            classes_serializer.save()
            return JsonResponse('Class Updated Successfully!', safe=False)
        return JsonResponse('Class modificaiton failed', safe=False)
    elif request.method=='DELETE':
        classes = Classes.objects.get(ClassId=id)
        classes.delete()
        return JsonResponse('Class Deleted Successfully!', safe=False)
    return JsonResponse('Class Deletion Failed',  safe=False)

@csrf_exempt
def studentsApi(request, id=0):
    if request.method=='GET':
        students = Students.objects.all()
        students_serializer = StudentsSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)
    elif request.method=='POST':
        students_data = JSONParser().parse(request)
        students_serializer = StudentsSerializer(data=students_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse('Student Added Successfully!', safe=False)
        return JsonResponse('Failed to add student', safe=False)
    elif request.method=='PUT':
        students_data = JSONParser().parse(request)
        students = Students.objects.get(StudentId=students_data['StudentId'])
        students_serializer = StudentsSerializer(students, data=students_data)
        if students_serializer.is_valid():
            students_serializer.save()
            return JsonResponse('Student updated successfully!', safe=False)
        return JsonResponse('Student modification failed', safe=False)
    elif request.method=='DELETE':
        students = Students.objects.get(StudentId=id)
        students.delete()
        return JsonResponse('Student deleted successfully!', safe=False)
    return JsonResponse('Student deletion failed', safe=False)

@csrf_exempt
def SavePhoto(request):
    file=request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name,safe=False)
