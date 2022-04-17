from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Vendor(models.Model):
    name = models.CharField(max_length=60)
    created_at = models.DateField(auto_now_add=True)
    created_by = models.OneToOneField(User, on_delete=models.CASCADE ,related_name="vendor")
    
    class Meta:
        ordering=['name']

    def __str__(self):
        return self.name