# -*- coding: utf-8 -*-

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Определим кастомную модель пользователя для возможных правок в будущем."""
    pass
