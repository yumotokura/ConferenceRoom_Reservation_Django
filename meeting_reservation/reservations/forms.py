from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reserved_by', 'start_time', 'end_time']
        labels = {
            'reserved_by': '名前',
            'start_time': '開始時間',
            'end_time': '終了時間',
        }
        widgets = {
            'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }
