from django.db import models

# Create your models here.
class Classes(models.Model):
    ClassId = models.AutoField(primary_key=True)
    ClassName = models.CharField(max_length=100)

class Students(models.Model):
    StudentId = models.AutoField(primary_key=True)
    StuentName = models.CharField(max_length=100)
    ClassId = models.ForeignKey(Classes, on_delete=models.CASCADE)
    DateOfBirth = models.DateField()
    PhotoFileName = models.CharField(max_length=100)

