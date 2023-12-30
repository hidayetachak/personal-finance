from django.db import models
from django.contrib.auth.models import User

class Earnings(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    source = models.TextField()
    date = models.DateField()

class Expenses(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    date = models.DateField()
def __str__(self):
     return self.title
class Service(models.Model):
    client_name = models.CharField(max_length=100)
    client_phone = models.CharField(max_length=15)
    client_email = models.EmailField()
    service_description = models.CharField(max_length=255)
    months_valid = models.IntegerField()
    due_date = models.DateField()
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.client_name} - {self.service_description}"