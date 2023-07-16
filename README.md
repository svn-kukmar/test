# Employee Management System

The Employee Management System is a Django-based web application that facilitates the management of employees within an organization. The application provides functionality for managing departments, employees, salaries, and tasks.

The system is built with Django 4.2.3 and the Django Rest Framework 3.14.0.

## Applications

The system is composed of the following Django apps:

1. **Department**: Manages the different departments within an organization.
2. **Employee**: Manages the employees, their roles, their managers, and their associated departments.
3. **Salary**: Manages the salaries of each employee.
4. **Task**: Manages tasks assigned to employees, including status and deadline information.

Each of these apps includes a `models.py` file to define the data structure, and a `views.py` file to handle the application logic.

## API Endpoints

Each application provides several API endpoints for creating, retrieving, updating, and deleting resources. These endpoints follow the principles of REST.

The following main endpoints are available:

- `/api/department/`: Manage departments.
- `/api/employee/`: Manage employees.
- `/api/salary/`: Manage salaries.
- `/api/task/`: Manage tasks.

Data can be added via two methods:

1. **Frontend Forms**: The project includes HTML forms for each model, which can be accessed via the associated URL.
2. **Postman**: If you prefer not to use the frontend or need to automate the process, you can use Postman or a similar API client to make HTTP requests to the provided endpoints.

## Installation and Setup

You need to have Python installed on your machine.

1. **Clone the repository**
1.https://github.com/vishodhan123/Employee_management1.git
