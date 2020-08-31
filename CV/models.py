from django.conf import settings
from django.db import models
# Create your models here.

class CVpost(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # name "Owain Edwards"
    homeAddress = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    contactNumber = models.CharField(max_length=13)
    # Current Status
    status = models.CharField(max_length=200)

    # About me
    aboutMe = models.TextField()

# Models that will have things added to.
class Qualifications(models.Model):
    qualification = models.CharField(max_length=200)

class Projects(models.Model):
    projectTitle = models.CharField(max_length=200)
    projectDescription = models.TextField()
