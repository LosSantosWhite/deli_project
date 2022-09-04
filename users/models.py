from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    surname = models.CharField(verbose_name='Отчество', max_length=20, null=True, blank=True)
    phone_number = models.CharField(verbose_name='Номер телефона', null=True, blank=True,
                                    max_length=12,)
