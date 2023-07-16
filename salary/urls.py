from django.urls import path
from . import views
from .views import SalaryUI, SalaryAPI

app_name = 'salary'


urlpatterns = [
    path('api/salary/', SalaryAPI.as_view()),
    path('salary-ui/', SalaryUI.as_view(), name='salary-ui'),

]