from django.db import models

# Create your models here.
class Student(models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()
    
    def __str__(self)->str:
        return self.FirstName