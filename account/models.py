from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    class Meta:
        verbose_name = 'Расширенный профиль пользователя'
        verbose_name_plural = 'Расширенные профили пользователей'
        
    user = models.OneToOneField(
        verbose_name='Пользователь',
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile',
    )
    info = models.TextField(
        verbose_name='О себе',
        blank=True,
        null=True,
    )
    avatar = models.ImageField(
        verbose_name='Фото профиля',
        upload_to='avatars/',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f'Профиль пользователя {self.user.username}'