from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    views = models.IntegerField(default=0)
