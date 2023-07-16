from django.db import connection
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import default_storage


class EmployeeView(APIView):
    parser_classes = (MultiPartParser,)

    def get(self, request):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM employee_employee")
            rows = self.dictfetchall(cursor)
        return Response(rows)

    def post(self, request):
        name = request.data.get('name')
        department_id = request.data.get('department')
        role = request.data.get('role')
        manager_id = request.data.get('manager')
        id_document = request.FILES.get('identification_document')

        with connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO employee_employee (name, department_id, role, manager_id, identification_document) "
                "VALUES (%s, %s, %s, %s, %s)",
                [name, department_id, role, manager_id, id_document.name])

        id_document_path = default_storage.save(id_document.name, id_document)

        return Response({'message': 'Employee added successfully!', 'document_path': id_document_path},
                        status=status.HTTP_201_CREATED)

    def dictfetchall(self, cursor):
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]


class EmployeeUI(TemplateView):
    template_name = 'employee/employee-ui.html'
