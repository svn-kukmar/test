from django.urls import path
from . import views
from .views import TaskAPI, TaskUI

app_name = 'task'


urlpatterns = [
    path('api/task/', TaskAPI.as_view()),
    path('task-ui/', TaskUI.as_view(),name='task-ui'),

]