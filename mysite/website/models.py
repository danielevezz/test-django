import datetime
from django.db import models


# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=50)
    createdAt = models.DateTimeField("Created at")
    description = models.TextField("description")

    def __str__(self):
        return self.title

    def new(self):
        delta = datetime.datetime.now() - self.createdAt.replace(tzinfo=None)
        return delta.days <= 2
