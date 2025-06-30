from django.urls import path
from . import views

urlpatterns = [
    path('packages/', views.packages_view, name='packages'),
     path('book_package/<int:package_id>/', views.book_package, name='book_package'),
    path('my-bookings/', views.user_bookings, name='user_bookings'),  # New URL for user bookings
]