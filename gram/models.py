from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.

#class Profile
class Profile(models.Model):
    picture = CloudinaryField('image')
    bio = models.TextField()


#class Images
class Image(models.Model):
    image = CloudinaryField('images')
    image_name = models.CharField(max_length=30,blank=True)
    image_caption = models.CharField(max_length=300)
    profile = models.ForeignKey(Profile,on_delete = models.CASCADE)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )
    comments = models.CharField(max_length=30,blank=True)

    def __str__(self):
        return self.image_name

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


   
