from django.db import models


from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=200, null=False)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=200, null=False)
    last = models.CharField(max_length=200)
    dept = models.ForeignKey(Department, on_delete=models.PROTECT,db_constraint=False)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    phone = models.IntegerField(default=0)
    role = models.ForeignKey(Role, on_delete=models.PROTECT,db_constraint=False)

    def __str__(self):
        return "%s %s %s" % (self.first_name, self.last, self.phone)
