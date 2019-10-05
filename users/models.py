from PIL import Image
from django.contrib.auth.models import User, AbstractUser
from django.db import models

from admissionnews.models import University


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dateOfBirth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True, null=True)
    fullName = models.CharField(max_length=100, blank=True, null=True)
    # lastName = models.CharField(max_length=100, blank=True, null=True)
    # fathersName = models.CharField(max_length=100, blank=True, null=True)
    # mothersName = models.CharField(max_length=100, blank=True, null=True)
    sscRollNo = models.IntegerField(unique=True, blank=True, null=True)
    sscRegiNo = models.IntegerField(unique=True, blank=True, null=True)
    sscGPA = models.FloatField(unique=True, blank=True, null=True)
    hscRollNo = models.IntegerField(unique=True, blank=True, null=True)
    hscGPA = models.FloatField(unique=True, blank=True, null=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', null=True)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
