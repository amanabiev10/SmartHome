from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    display_name = models.CharField(max_length=255, blank=True)
    registered = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)

    def get_display_name(self):
        return self.display_name

    def save(self, *args, **kwargs):
        if not self.pk:
            self.display_name = f'{self.last_name} {self.first_name}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Benutzer'
        verbose_name_plural = 'Benutzern'
