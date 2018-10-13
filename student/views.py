from django.shortcuts import render
from .models import StudentInfo


def student_list(request):
    std_list = StudentInfo.objects.all()
    context = {'students': std_list}
    return render(request, 'student/student_list.html', context)


def student_detail(request, std_roll):
    std = StudentInfo.objects.get(roll=std_roll)
    context = {'student': std}
    return render(request, 'student/student_detail.html', context)


def class_wise_student(request, class_no):
    std_list = StudentInfo.objects.filter(std_class=class_no)
    context = {'students': std_list}
    return render(request, 'class_wise_std.html', context)