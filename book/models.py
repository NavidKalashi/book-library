from django.db import models
from django.contrib.auth.models import User
import uuid

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.IntegerField(default=0, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    category = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title