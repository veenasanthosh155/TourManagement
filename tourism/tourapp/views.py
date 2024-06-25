from django.shortcuts import render,redirect
from tourapp.models import Package,Booking
from tourapp.forms import BookingForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

@login_required
def packages(request):
    p = Package.objects.all()
    return render(request,'packages.html',{'p':p})
@login_required
def details(request,p):
    p = Package.objects.filter(name=p)
    return render(request, 'details.html', {'p':p})

@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tourapp:booking')  # redirect to the confirm page after saving
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

@login_required
def confirm(request):
    k=Booking.objects.all()
    return render(request,'confirm.html',{'k':k})

@login_required
def edit(request, p):
    b = Booking.objects.get(id=p)
    if request.method == "POST":
        form = BookingForm(request.POST,instance=b)
        if form.is_valid():
            form.save()
            return redirect('tourapp:confirm')  # redirect to the confirm page after editing

    else:
        form = BookingForm(instance=b)
    return render(request, 'edit.html', {'form': form})


@login_required
def delete(request,p):
    b=Booking.objects.get(id=p)
    b.delete()
    return confirm(request)

@login_required
def order(request):
    if request.method == 'POST':
        booking_id = request.POST.get('booking_id')
        bookings = Booking.objects.get(id=booking_id)
        bookings.delete()
        msg = "Booking confirmed successfully!"
        return render(request, 'order.html', {'msg': msg})
    else:
        return redirect('tourapp:confirm')




