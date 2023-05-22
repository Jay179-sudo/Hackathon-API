from django.contrib import admin

# Register your models here.
from .models import Hackathon, Submission, Enrollment

admin.site.register(Hackathon)
admin.site.register(Submission)
admin.site.register(Enrollment)