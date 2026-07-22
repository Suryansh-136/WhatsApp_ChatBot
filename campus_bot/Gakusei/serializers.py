from rest_framework.serializers import ModelSerializer
from .models import (StudentProfile,Attendance,Notice,Timetable) 
from rest_framework import serializers

class StudentProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username",
        read_only=True
    )

    email = serializers.EmailField(
        source="user.email",
        read_only=True
    )

    class Meta:
        model = StudentProfile
        fields = [
            "username",
            "email",
            "enrollment_no",
            "branch",
            "semester",
            "phone_number",
        ]

class AttendanceSerializer(serializers.ModelSerializer):
    subject = serializers.CharField(source="subject_name")
    percentage = serializers.SerializerMethodField()

    class Meta:
        model = Attendance
        fields = [
            "subject",
            "attended_classes",
            "total_classes",
            "percentage",
        ]

    def get_percentage(self, obj):
        if obj.total_classes == 0:
            return 0
        return round(
            obj.attended_classes / obj.total_classes * 100,
            2
        )


class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = [
            "id",
            "title",
            "content",
            "created_at",
        ]



class TimetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timetable
        fields = [
            "day",
            "subject_name",
            "start_time",
            "end_time",
        ]
        ordering = ["day", "start_time"]