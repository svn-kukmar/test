from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.db import connection
from django.urls import reverse
from django.views.generic import TemplateView
from rest_framework.response import Response
from rest_framework.views import APIView


# def homepage(request):
#     return render(request=request, template_name='department/base.html')
#
#
# def department_add(request):
#     return render(request=request, template_name='department/create_department.html')


def department_list(request):
    if request.method == 'POST':
        # Get the department name from the form
        name = request.POST.get('name')

        # Execute an SQL INSERT query to create a new department
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO department_department (name) VALUES (%s)", [name])

        # Redirect to the department list URL
        # return redirect('department_list')
        return HttpResponseRedirect(reverse("department:department_list", kwargs={}))

    if request.method == 'GET':
        # Execute an SQL SELECT query to retrieve all departments
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM department_department")
            departments = cursor.fetchall()
            print(departments)

        return render(request, 'department/department_list.html', {'departments': departments})


class DepartmentAPI(APIView):
    def post(self, request):
        # Get the department name from the form
        name = request.data.get('name')

        # Execute an SQL INSERT query to create a new department
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO department_department (name) VALUES (%s)", [name])

        # return redirect('department_list')
        return Response({"data": {"message": "Data inserted successfully"}}, status=201)

    def get(self, request):
        result = []
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM department_department")
            departments = cursor.fetchall()
            for dep in departments:
                result.append({"id": dep[0], "name": dep[1]})
        return Response({"data": result}, status=200)


class Homepage(TemplateView):
    template_name = 'home.html'


class DepartmentUI(TemplateView):
    template_name = 'departments/department_ui.html'

