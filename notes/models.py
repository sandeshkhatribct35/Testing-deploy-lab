from django.db import models
from django.core.exceptions import ValidationError

class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def clean(self):
        if len(self.description) < 10:
            raise ValidationError("Description must be at least 10 characters long")

    def __str__(self):
        return self.title