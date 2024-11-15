from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    name = models.CharField(max_length=255)
    deadline = models.DateField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.name
