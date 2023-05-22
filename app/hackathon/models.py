# models.py

from django.db import models
from django.conf import settings

class Hackathon(models.Model):
    TYPE_CHOICES = [
        ('image', 'Image'),
        ('file', 'File'),
        ('link', 'Link'),
    ]

    title = models.CharField(max_length=255, primary_key=True)
    description = models.TextField()
    background_image = models.ImageField(upload_to='mediafiles/')
    hackathon_image = models.ImageField(upload_to='mediafiles/')
    type_of_submission = models.CharField(max_length=5, choices=TYPE_CHOICES)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    reward_prize = models.DecimalField(max_digits=8, decimal_places=2)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title[:50]



class Submission(models.Model):
    name = models.CharField(max_length=255, unique=True)
    summary = models.TextField()
    submission_file = models.FileField(upload_to='mediafiles/', blank=True, null=True)
    submission_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name[:50]
    
class Enrollment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    hackathon = models.ForeignKey(Hackathon, on_delete=models.CASCADE)