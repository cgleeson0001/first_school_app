from django.db import models
from datetime import datetime


# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=400)
    address = models.CharField(max_length=400)
    postal_code = models.IntegerField()

    def __str__(self):
        return self.name
      
class Certificate(models.Model):
    name = models.CharField(max_length = 400)

    def __str__(self):
        return self.name

class Faculty(models.Model):
    name = models.CharField(max_length = 400)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length = 400)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Grade(models.Model):
    type = models.IntegerField

    def __str__(self):
        return self.name

class Student(models.Model):
    full_name = models.CharField(max_length = 40)
    year_of_graduation = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True)
    School = models.ForeignKey(School, on_delete=models.CASCADE)
    certificate_type = models.ForeignKey(Certificate, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name, self.year_of_graduation, self.department, self.grade,