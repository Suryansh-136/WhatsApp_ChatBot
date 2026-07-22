from .models import (StudentProfile,Attendance,Notice,Timetable)
from .serializers import (StudentProfileSerializer,AttendanceSerializer,NoticeSerializer,TimetableSerializer)
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.generics import RetrieveAPIView
#from rest_framework.permissions import IsAuthenticated

class StudentProfileAPIView(RetrieveAPIView):
    serializer_class = StudentProfileSerializer

    def get_object(self):
        return StudentProfile.objects.get(
            user=self.request.user
        )
# class StudentCreateAPIView(CreateAPIView):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer

class MyAttendanceAPIView(ListAPIView):
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        return Attendance.objects.filter(
            student__user=self.request.user
        )

class NoticeListAPIView(ListAPIView):
    serializer_class = NoticeSerializer

    def get_queryset(self):
        return Notice.objects.order_by("-created_at")


class MyTimetableAPIView(ListAPIView):
    serializer_class = TimetableSerializer

    def get_queryset(self):
        student = self.request.user.student_profile

        return Timetable.objects.filter(
            semester=student.semester)
            