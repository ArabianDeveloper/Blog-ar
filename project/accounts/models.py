from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_countries.fields import CountryField
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    city = CountryField()
    phone_number = models.CharField(max_length=15)
    image = models.ImageField(upload_to = 'profile' , default = 'images/mim-logo.png')

    def __str__(self):
        return str(self.user)
## create new user --> 

@receiver(post_save, sender=User)
def create_user_profile(sender , instance , created , **kwargs):
    if created:
        Profile.objects.create(user = instance)

