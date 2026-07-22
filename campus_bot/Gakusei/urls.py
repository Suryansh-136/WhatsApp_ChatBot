from .views import (StudentProfileAPIView,MyAttendanceAPIView,NoticeListAPIView,MyTimetableAPIView)
from django.urls import path
urlpatterns=[
    path('my-profile/', StudentProfileAPIView.as_view(),name='my-profile'),

    #path('create-student/',StudentCreateAPIView.as_view()),

    path('my-attendance/',MyAttendanceAPIView.as_view(), name='my-attendance'),

    path('notices/', NoticeListAPIView.as_view(),name='notices'),

    path('my-timetable/', MyTimetableAPIView.as_view(),name='my-timetable'),

]