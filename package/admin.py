from django.contrib import admin
from .models import Package, Booking

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'package', 'date', 'status')
    list_filter = ('status', 'date')
    actions = ['confirm_booking', 'decline_booking']

    def confirm_booking(self, request, queryset):
        queryset.update(status='confirmed')
        self.message_user(request, "Selected bookings have been confirmed.")
    confirm_booking.short_description = "Confirm selected bookings"

    def decline_booking(self, request, queryset):
        queryset.update(status='declined')
        self.message_user(request, "Selected bookings have been declined.")
    decline_booking.short_description = "Decline selected bookings"
