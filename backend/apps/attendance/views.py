from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance
from apps.employees.models import Employee


class AttendanceListCreateView(APIView):

    def get(self, request):
        attendance = Attendance.objects.all().values()
        return Response(attendance)

    def post(self, request):
        try:
            employee_id = request.data.get("employee_id")
            date = request.data.get("date")
            status_value = request.data.get("status")

            employee = Employee.objects.get(employee_id=employee_id)

            attendance = Attendance.objects.create(
                employee=employee,
                date=date,
                status=status_value
            )

            return Response({"message": "Attendance marked successfully"}, status=status.HTTP_201_CREATED)

        except Employee.DoesNotExist:
            return Response({"error": "Employee not found"}, status=status.HTTP_400_BAD_REQUEST)
