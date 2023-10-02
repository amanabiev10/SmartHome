from django import forms
from .models import Lamp


class LampForm(forms.ModelForm):
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

    color = forms.ChoiceField(choices=COLOR_CHOICES, label='Farbe')

    class Meta:
        model = Lamp
        fields = ['name', 'status', 'color', 'brightness', 'schedule_on', 'schedule_off']

    def clean_brightness(self):
        brightness = self.cleaned_data.get('brightness')
        if brightness < 0 or brightness > 100:
            raise forms.ValidationError('Die Helligkeit muss zwischen 0 und 100 liegen.')
        return brightness
