from django.db import models

# Test Models
class Test(models.Model):
    name = models.CharField(max_length=30)