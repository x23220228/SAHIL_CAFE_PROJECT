from django import forms
from .models import Reservation
from django.utils import timezone

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'mobile', 'people', 'datetime']
        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['datetime'].input_formats = ('%Y-%m-%dT%H:%M',)

    def clean(self):
        cleaned_data = super().clean()
        datetime = cleaned_data.get('datetime')
        if datetime and datetime < timezone.now():
            raise forms.ValidationError("Reservation date and time cannot be in the past.")
        return cleaned_data