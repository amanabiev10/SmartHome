from django.db import models
from django.contrib.auth.models import Permission
from accounts.models import User
from decimal import Decimal
from django.utils import timezone


class Lamp(models.Model):
    COLOR_CHOICES = [
        ('#ffffff', 'Weiß'),
        ('#000000', 'Schwarz'),
        ('#ff0000', 'Rot'),
        ('#00ff00', 'Grün'),
        ('#0000ff', 'Blau'),
        ('#ffff00', 'Gelb'),
        ('#ff00ff', 'Magenta'),
        ('#ffa500', 'Orange'),
        ('#a52a2a', 'Braun'),
        ('#808080', 'Grau'),
        ('#ff69b4', 'Rosa'),
        ('#ff4500', 'Orange-Rot'),
        ('#2f4f4f', 'Dunkelgrau'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='lamps')
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    color = models.CharField(max_length=7, choices=COLOR_CHOICES, default='#ffffff')
    brightness = models.PositiveIntegerField(default=50)
    schedule_on = models.TimeField(null=True, blank=True)
    schedule_off = models.TimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def calculate_energy_consumption(self):
        try:
            brightness_factor = float(self.brightness) / 100.0
        except ValueError:
            brightness_factor = 2.0  # Beispielwert für den Fall, dass die Konvertierung fehlschlägt

        base_consumption = 5.0

        energy_consumption = base_consumption + (brightness_factor * 10.0)

        return energy_consumption

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Wenn sich der Status ändert, aktualisiere die LampStatistics
        if self.status:
            try:
                statistics = self.statistics
            except LampStatistics.DoesNotExist:
                statistics = LampStatistics(lamp=self)

            energy_consumption = self.calculate_energy_consumption()
            statistics.energy_consumption = Decimal(energy_consumption)
            statistics.usage_duration = timezone.timedelta(seconds=60)
            statistics.save()

    def __str__(self):
        return self.name


class LampStatistics(models.Model):
    lamp = models.OneToOneField(Lamp, on_delete=models.CASCADE, related_name='statistics')
    timestamp = models.DateTimeField(auto_now_add=True)
    energy_consumption = models.DecimalField(max_digits=8, decimal_places=2)
    usage_duration = models.DurationField()

    @classmethod
    def create_statistics(cls, lamp):
        energy_consumption = lamp.calculate_energy_consumption()
        cls.objects.create(
            lamp=lamp,
            energy_consumption=Decimal(energy_consumption),
            usage_duration=timezone.timedelta(seconds=60)
        )

    def __str__(self):
        return f'Statistics for {self.lamp.name} at {self.timestamp}'
