from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()


class DashboardData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=10, decimal_places=2)
    income_goal = models.DecimalField(max_digits=10, decimal_places=2)
    RISK_CHOICES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    risk = models.CharField(max_length=10, choices=RISK_CHOICES)
