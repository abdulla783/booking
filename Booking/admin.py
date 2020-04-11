from django.contrib import admin
from Booking.models import roomBooking
# Register your models here.

class roomBookingAdmin(admin.ModelAdmin):
    list_display = ('booking_id',
                    'customer_first_name',
                    'customer_last_name',
                    'gender',
                    'customer_email')
    list_display_links = ('booking_id', 'customer_first_name',)

admin.site.register(roomBooking, roomBookingAdmin)
