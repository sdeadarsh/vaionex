from django.db import models
from wiki import config



# Create your models here.

class Title(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        db_table = "title"


class Document(models.Model):
    title_id = models.PositiveIntegerField()
    timestamp = models.PositiveIntegerField(null=True, blank=True)
    content = models.CharField(max_length=500, null=True, blank=True)
