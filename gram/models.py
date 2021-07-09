from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.

#class Profile
class Profile(models.Model):
    picture = CloudinaryField('image')
    bio = models.TextField()