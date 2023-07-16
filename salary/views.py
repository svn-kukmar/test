from django.db import connection
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SalaryAPI(APIView):

    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM salary_salary")
            salaries = self.dictfetchall(cursor)

        return Response(salaries, status=status.HTTP_200_OK)

    def post(self, request):
        employee_id = request.data.get('employee_id')
        amount = request.data.get('amount')
        date = request.data.get('date')

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO salary_salary (employee_id, amount, date) VALUES (%s, %s, %s)",
                [employee_id, amount, date]
            )

        return Response({"message": "Salary added successfully"}, status=status.HTTP_201_CREATED)

    def dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


class SalaryUI(TemplateView):
    template_name = 'salary/salary-ui.html'
