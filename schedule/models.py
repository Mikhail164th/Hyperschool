from django.db import models
from django.urls import reverse


# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=225)
    info = models.TextField(blank=True)
    duration_months = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    teacher = models.ManyToManyField("Teacher", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course_detail", kwargs={"pk": self.id})


class Student(models.Model):
    name = models.CharField(max_length=51)
    surname = models.CharField(max_length=51)
    age = models.IntegerField()
    course = models.ManyToManyField("Course", blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

class Teacher(models.Model):
    name = models.CharField(max_length=51)
    surname = models.CharField(max_length=51)
    age = models.IntegerField()
    about = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_absolute_url(self):
        return reverse(viewname="teacher_detail", kwargs={"pk": self.id})