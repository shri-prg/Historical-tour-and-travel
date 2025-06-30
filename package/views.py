from django.shortcuts import render, redirect, get_object_or_404
from .models import Package, Booking
from django.contrib.auth.decorators import login_required

def packages_view(request):
    packages = Package.objects.all()  # Fetch all packages from the database
    return render(request, 'packages.html', {'packages': packages})

@login_required
def book_package(request, package_id):
    package = get_object_or_404(Package, id=package_id)  # Get the package by ID or return 404

    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')  # Get the selected date from the form
        # Create a booking with the selected date
        Booking.objects.create(user=request.user, package=package, date=booking_date)
        return redirect('user_bookings')  # Redirect to the user's booking page

    # Render the booking form if the request is GET
    return render(request, 'book_package.html', {'package': package})

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)  # Fetch bookings for the logged-in user
    return render(request, 'user_bookings.html', {'bookings': bookings})
