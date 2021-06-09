from django.shortcuts import render
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
class EmployeeView:
    @api_view(['GET'])
    def employeeDetails(request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many = True)
        return Response(serializer.data)

    @api_view(['GET'])
    def employeeDetailById(request, ids):
        employee = Employee.objects.get(id = ids)
        serializer = EmployeeSerializer(employee, many = False)
        return Response(serializer.data)

    @api_view(['POST'])
    def employeeCreate(request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['PUT'])
    def employeeUpdate(request, ids):
        employee = Employee.objects.get(id = ids)
        serializer = EmployeeSerializer(instance = employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['DELETE'])
    def employeeDelete(request, ids):
        employee = Employee.objects.get(roll = ids)
        employee.delete()
        return Response('Deleted')





