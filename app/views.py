from django.shortcuts import render, get_object_or_404, redirect
from .models import teachingClass, Student

def home(request):
    teachingclass = teachingClass.objects.all()  
    context = {'teachingClass': teachingclass}
    return render(request, 'home.html', context)

def student_list(request, class_id):
    teaching_class = get_object_or_404(teachingClass, id=class_id)
    students = Student.objects.filter(teaching_class=teaching_class)
    return render(request, 'studentList.html', {'teaching_class': teaching_class, 'students': students})

def give_merit(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.merits += 1
    student.save()
    return redirect('student_list', student.teaching_class.id)  # Redirect with correct class ID

def give_behavior_points(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.behaviour_points += 1
    student.save()
    return redirect('student_list', student.teaching_class.id)

