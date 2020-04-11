from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from Booking.forms import RoomBookingForm
from django.contrib import messages
from Booking.models import roomBooking


# Create your views here.

def homePage(request):
    return render(request, 'Booking/homePage.html')

def walkIn(request):
    if request.method == 'POST':
        customer_first_name = request.POST.get('fname',)
        customer_last_name = request.POST.get('lname',)
        gender = request.POST.get('gender',)
        customer_email = request.POST.get('email',)
        check_in_date = request.POST.get('check-in',)
        check_out_date = request.POST.get('check-out',)
        room = request.POST.get('room',)
        booking = roomBooking(customer_first_name=customer_first_name, customer_last_name=customer_last_name, gender=gender, customer_email=customer_email, check_in_date=check_in_date, check_out_date=check_out_date, room=room)
        booking.save()
        book_id = booking.booking_id
        print(book_id)
        messages.success(request, f'Booking has done. Your booking id is {book_id}')
        return redirect('/booking/already-booked/')
    # context = {
    #     'booking': booking
    # }   
    return render(request, 'Booking/walkIn.html')

def alreadyBooked(request):
    if request.method == "POST":
        book_id = request.POST.get('booking_id',)
        # booking = roomBooking.objects.filter(booking_id=book_id)
        booking = get_object_or_404(roomBooking, booking_id=book_id)
        context = {
            'booking': booking,
        }
        return render(request, 'Booking/bookingDetail.html', context)
    return render(request, 'Booking/alreadyBooked.html')

