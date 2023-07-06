from django.db import models

# Create your models here.
class Finch(models.Model):
    type = models.CharField(max_length=50)
    color = models.CharField(max_length=40)
    info = models.TextField(max_length=200)

    def __str__(self):
        return self.type