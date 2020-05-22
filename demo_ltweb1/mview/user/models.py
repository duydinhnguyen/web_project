from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

Sex_choice = (
    ('Nam', 'Nam'),
    ('Nữ', 'Nữ'),
    ('Không xác định', 'Không xác định'),
)


class ProfileUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profiles_pic', blank=True)
    sex = models.CharField(choices=Sex_choice, blank=True, max_length=20)
    birthday = models.DateField()

    def __str__(self):
        return {self.user.username}
