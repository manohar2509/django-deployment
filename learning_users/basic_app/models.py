from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    portofolio_site = models.URLField(blank='False')
    profile_pic = models.ImageField(blank='False',upload_to = 'profile_pics')
    def __str__(self):
        return self.user.username
