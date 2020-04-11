from django.urls import path
from Booking import views

app_name = "Booking"
urlpatterns = [
    path('walk-in/', views.walkIn, name='walkIn'),
    path('already-booked/', views.alreadyBooked, name='alreadyBooked'),
]