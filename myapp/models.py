from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    isdn = models.IntegerField()
    genre = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    class Meta:
        db_table = 'books'