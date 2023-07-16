from django.urls import path
from . import views
from .views import department_list, DepartmentAPI,  DepartmentUI

from django.views.generic import TemplateView

app_name = 'department'

urlpatterns = [
    path('api/department/', DepartmentAPI.as_view(), name='department-api'),
    path('department-ui/', DepartmentUI.as_view(), name='department-ui'),

]


