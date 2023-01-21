from django.db import models
import uuid

# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

  def __str__(self):
    return f"{self.firstname} {self.lastname}"

class Employee(models.Model):
  name    = models.CharField(max_length=200)
  email   = models.EmailField()
  contact = models.CharField(max_length=20)
  role    = models.CharField(max_length=200)
  salary  = models.IntegerField()
  id      = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
  def __str__(self):
    return self.name

class Person(models.Model):
  name    = models.CharField(max_length=200)
  marks   = models.IntegerField()
  def __str__(self):
    return self.name   # def __str__ (self) function is used to show the name in the admin

