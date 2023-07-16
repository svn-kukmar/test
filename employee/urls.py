from django.urls import path
from .views import EmployeeView, EmployeeUI

app_name = 'employee'

urlpatterns = [
    path('api/employee/', EmployeeView.as_view(), name='employee-api'),
    path('employee-ui/', EmployeeUI.as_view(), name='employee-ui'),

]
