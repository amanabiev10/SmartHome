from django.db import models
from django.contrib.auth.models import Permission
from accounts.models import User


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
        ('#800080', 'Lila'),
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

    def __str__(self):
        return self.name

    def turn_on(self):
        self.status = True
        self.save()

    def turn_off(self):
        self.status = False
        self.save()

    def get_status(self):
        return self.status

    def set_brightness(self, brightness):
        brightness = max(0, min(brightness, 100))
        self.brightness = brightness
        self.save()

    def get_brightness(self):
        return self.brightness

    def set_color(self, color):
        self.color = color
        self.save()

    def get_color(self):
        return self.color

    def set_schedule_on(self, time):
        self.schedule_on = time
        self.save()

    def get_schedule_on(self):
        return self.schedule_on

    def set_schedule_off(self, time):
        self.schedule_off = time
        self.save()

    def get_schedule_off(self):
        return self.schedule_off


class LampStatistics(models.Model):
    lamp = models.ForeignKey(Lamp, on_delete=models.CASCADE, related_name='statistics')
    timestamp = models.DateTimeField(auto_now_add=True)
    energy_consumption = models.DecimalField(max_digits=8, decimal_places=2)
    usage_duration = models.DurationField()

    def __str__(self):
        return f'Statistics for {self.lamp.name} at {self.timestamp}'

    @classmethod
    def add_statistics(cls, lamp, energy_consumption, usage_duration):
        # Diese Methode fügt neue Statistiken für eine Lampe hinzu
        cls.objects.create(lamp=lamp, energy_consumption=energy_consumption, usage_duration=usage_duration)

    @classmethod
    def get_statistics_for_lamp(cls, lamp):
        # Diese Methode ruft alle Statistiken für eine bestimmte Lampe ab
        return cls.objects.filter(lamp=lamp)

    @classmethod
    def get_total_energy_consumption_for_lamp(cls, lamp):
        # Diese Methode berechnet der Gesamtenergieverbrauch für eine Lampe
        statistics = cls.get_statistics_for_lamp(lamp)
        total_energy_consumption = sum(stat.energy_consumption for stat in statistics)
        return total_energy_consumption

    @classmethod
    def get_total_usage_duration_for_lamp(cls, lamp):
        # Diese Methode berechnet die Gesamtnutzungsdauer für eine Lampe
        statistics = cls.get_statistics_for_lamp(lamp)
        total_usage_duration = sum(stat.usage_duration for stat in statistics)
        return total_usage_duration
