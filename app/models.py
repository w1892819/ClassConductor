from django.db import models

class teachingClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20, unique=True)
    behaviour_points = models.IntegerField(default=0)
    merits = models.IntegerField(default=0)
    teaching_class = models.ForeignKey(teachingClass, related_name='students', on_delete=models.CASCADE)  
    
    def __str__(self):
        return f'{self.name} ({self.student_id})'
