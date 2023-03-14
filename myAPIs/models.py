
from django.db import models


class CSVData(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    pan = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name}, {self.age}, {self.birthdate}, {self.pan}"
