from django.db import models

# Create your models here.

class notes(models.Model):
    text = models.TextField()
    notes = models.TextField()
    created = models.DateTimeField(auto_now_add = True)