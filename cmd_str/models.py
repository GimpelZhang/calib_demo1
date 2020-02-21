from django.db import models

# Create your models here.
# models.py
from django.db import models

class CMD_CONTENT(models.Model):
    world_name = models.CharField(max_length=40)
