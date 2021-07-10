from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField



# Create your models here.

#class Profile
class Profile(models.Model):
    picture = CloudinaryField('image')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user

    @classmethod
    def update_profile(cls, id, user, bio, picture):
        cls.objects.filter(id=id).update(user=user, bio=bio, picture=picture)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()



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
    def update_image_caption(cls, id, image_caption):
        cls.objects.filter(id=id).update(image_caption=image_caption)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()


   
