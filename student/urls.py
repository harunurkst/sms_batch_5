from django.urls import path
from .views import student_list, student_detail

urlpatterns = [
    path('list/', student_list, name="student-list"),
    path('detail/<int:std_roll>', student_detail, name="student-detail")
]
