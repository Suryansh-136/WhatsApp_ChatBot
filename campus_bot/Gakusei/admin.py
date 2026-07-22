from django.contrib import admin
from .models import (StudentProfile, Attendance, Notice, Timetable, TelegramUser)


@admin.register(StudentProfile)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "enrollment_no",
        "branch",
        "semester",
    )


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "subject_name",
        "total_classes",
        "attended_classes",
    )


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_at",
    )


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = (
        "day",
        "subject_name",
        "start_time",
        "end_time",
    )


@admin.register(TelegramUser)
class TelegramUserAdmin(admin.ModelAdmin):
    list_display = (
        "student",
        "telegram_id",
        "linked_at",
    )

    search_fields = (
        "telegram_id",
        "student__enrollment_no",
        "student__user__username",
    )