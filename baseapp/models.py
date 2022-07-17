
from django.db import models

class Book(models.Model):
    bookTitle = models.CharField(max_length=50)