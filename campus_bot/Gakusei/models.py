from django.db import models
from django.contrib.auth.models import User



class StudentProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    enrollment_no = models.CharField(
        max_length=20,
        unique=True
    )

    branch = models.CharField(
        max_length=50
    )

    semester = models.PositiveIntegerField()

    phone_number = models.CharField(
        max_length=15,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.enrollment_no})"

# class for Attendance percentage
class Attendance(models.Model):
    student = models.ForeignKey(StudentProfile,
        on_delete=models.CASCADE,
        #related_name="attendance_records"
    )

    subject_name = models.CharField(max_length=100)

    total_classes = models.PositiveIntegerField()

    attended_classes = models.PositiveIntegerField()

    updated_at = models.DateTimeField(auto_now=True)

    def attendance_percentage(self):
        if self.total_classes == 0:
            return 0

        return round(
            (self.attended_classes / self.total_classes) * 100,
            2
        )

    def __str__(self):
        return f"{self.student.user.username} - {self.subject_name}"



# class for Notice
class Notice(models.Model):
    title = models.CharField(max_length=200)

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title


# class for Timetable
class Timetable(models.Model):

    DAY_CHOICES = [
        ("MONDAY", "Monday"),
        ("TUESDAY", "Tuesday"),
        ("WEDNESDAY", "Wednesday"),
        ("THURSDAY", "Thursday"),
        ("FRIDAY", "Friday"),
        ("SATURDAY", "Saturday"),
    ]

    semester = models.PositiveIntegerField()

    day = models.CharField(
        max_length=20,
        choices=DAY_CHOICES
    )

    subject_name = models.CharField(max_length=100)

    start_time = models.TimeField()

    end_time = models.TimeField()





class TelegramUser(models.Model):
    student = models.OneToOneField(
        StudentProfile,
        on_delete=models.CASCADE
    )

    telegram_id = models.BigIntegerField(
        unique=True
    )

    linked_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.student} - {self.telegram_id}"