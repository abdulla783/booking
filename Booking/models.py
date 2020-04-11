from django.db import models

# Create your models here.

class roomBooking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    customer_first_name = models.CharField(max_length=100)
    customer_last_name = models.CharField(max_length=100)
    gender_choices = [('M', 'Male'), ('F', 'Female')]
    gender = models.CharField(
                    choices=gender_choices,
                    max_length=6,
                    default=None,
                    null=True)
    customer_email = models.EmailField()
    check_in_date = models.DateField(max_length=10,
                                    help_text="format : YYYY-MM-DD",
                                    null=False)
    check_out_date = models.DateField(max_length=10,
                                    help_text="format : YYYY-MM-DD",
                                    null=False)
    room_choices = [('Single', 'Single'), ('Double', 'Double'), ('Large', ('Large'))]
    room = models.CharField(
                    choices=room_choices,
                    max_length=6,
                    default='Single',
                    null=True)
    
    def __str__(self):
        return self.customer_first_name
    
    
