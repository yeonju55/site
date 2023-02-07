from django.db import models
from django.contrib.auth.models import User
# Create your models here.

from django.contrib.auth import get_user_model

# user 확장
# (id, 비밀번호, 이메일, 이름, 전화번호, 주소)

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=13)
    address = models.CharField(max_length=100)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_images')
    bio = models.TextField()

    def __str__(self):
        return self.user.username

# 위치 중요!!! 무조건 class보다 아래에 있어야 함!
User = get_user_model()
