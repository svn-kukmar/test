from django.db import connection
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TaskAPI(APIView):
    def post(self, request):
        # Extract data from the request
        name = request.data.get('name')
        description = request.data.get('description')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        status = request.data.get('status')
        employee_id = request.data.get('employee_id')

        # Execute an SQL INSERT query to create a new task
        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO task_task (name, description, start_date, end_date, status, employee_id) VALUES (%s, %s, %s, %s, %s, %s)",
                [name, description, start_date, end_date, status, employee_id]
            )

        return Response({"message": "Task created successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        tasks = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM task_task")
            rows = cursor.fetchall()

            for row in rows:
                tasks.append({
                    'id': row[0],
                    'name': row[1],
                    'description': row[2],
                    'start_date': row[3],
                    'end_date': row[4],
                    'status': row[5],
                    'employee_id': row[6]
                })

        return Response(tasks, status=status.HTTP_200_OK)


class TaskUI(TemplateView):
    template_name = 'task/task-ui.html'
