from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from user.managers import CustomUserManager
import uuid

def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return f'uploads/user_images/{filename}'

class User(AbstractUser):
    is_curator = models.BooleanField(default=False)
    username = None
    middle_name = models.CharField(
        _("Отчество"),
        max_length=30,
        blank=True,
        null=True
    )
    email = models.EmailField(
        _("email address"),
        unique=True
    )
    phone_number = models.CharField(
        _("Номер телефона"),
        max_length=20,
        blank=True,
        null=True
    )
    photo = models.FileField(
        _("Фотография"),
        upload_to=get_file_path
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        if not self.last_name or not self.first_name:
            return f'{self.email}'
        if not self.middle_name:
            return f'{self.last_name} {self.first_name}'
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
