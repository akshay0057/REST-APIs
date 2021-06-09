from django.urls import path
from . import views
from .views import EmployeeView

urlpatterns = [
    path('details/', EmployeeView.employeeDetails, name = 'employeeDetails'),
    path('detailsById/<int:ids>/', EmployeeView.employeeDetailById, name = 'employeeDetailsById'),
    path('create/', EmployeeView.employeeCreate, name = 'createemployee'),
    path('update/<int:ids>/', EmployeeView.employeeUpdate , name = 'update'),
    path('delete/<int:ids>/', EmployeeView.employeeDelete , name = 'delete')
]