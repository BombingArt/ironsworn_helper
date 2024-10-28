from django.db import models
from datetime import datetime
from ironhelper import settings
from django.core.validators import MaxValueValidator


class Campaign(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.CASCADE, related_name='campaigns')
    supplies = models.IntegerField(
        default=5, validators=[MaxValueValidator(5)])

    def __str__(self):
        return f"{self.title} by {self.owner}"
