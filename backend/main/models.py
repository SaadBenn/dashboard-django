from django.db import models
from django.contrib.auth.models import User


class EmployeeRelation(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hierarchy_user')
    reporting_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hierarchy_manager')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class SalesLines(models.Model):
    rep = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sale_user')
    reporting_day = models.DateField()
    sku = models.TextField()
    revenue = models.DecimalField(max_digits=16, decimal_places=4)
    commission_rate = models.DecimalField(max_digits=16, decimal_places=4)
    earnings = models.DecimalField(max_digits=16, decimal_places=4)
