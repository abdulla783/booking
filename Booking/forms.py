from django import forms
from Booking.models import roomBooking


class RoomBookingForm(forms.ModelForm):
    check_in_date = forms.DateField(widget = forms.SelectDateWidget)
    check_out_date = forms.DateField(widget = forms.SelectDateWidget)
    class Meta:
        model = roomBooking
        fields = ('__all__')