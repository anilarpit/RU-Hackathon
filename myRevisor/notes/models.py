from django.db import models
# Create your models here.
from Profile.models import Profile

class Note(models.Model):
    importance_choices = (
        ('very important', 'very important'),
        ('important', 'important'),
        ('less important', 'less important')
    )
    topic = models.CharField(max_length=120)
    comment = models.TextField(blank=True)
    image = models.FileField(upload_to='img/')
    importance = models.CharField(max_length=20, choices=importance_choices, default='less important')
    profile = models.ForeignKey(Profile, null=True, on_delete=models.CASCADE)


