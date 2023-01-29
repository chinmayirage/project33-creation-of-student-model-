from django.db import models

# Create your models here.
class Student(models.Model):
    SNO=models.IntegerField(max_length=10,primary_key=True)
    Name=models.CharField(max_length=100)
    Age=models.IntegerField(max_length=2)
    Email=models.CharField(max_length=100)
    Marks=models.IntegerField(max_length=3)

    def __str__(self):
        return self.Name


class Employee(models.Model):
    Empno=models.IntegerField(max_length=5)
    Deptno=models.IntegerField(max_length=5)
    Name=models.CharField(max_length=100)
    Salary=models.IntegerField(max_length=10)

    def __str__(self):
        return self.Name
