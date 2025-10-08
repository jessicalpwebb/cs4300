from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    MovieViewSet, SeatViewSet, BookingViewSet,
    movie_list, seat_booking, booking_history
)

router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('', movie_list, name='movie_list'),  # movies.html
    path('book/<int:movie_id>/', seat_booking, name='seat_booking'),  # seats.html
    path('history/', booking_history, name='booking_history'),  # previous_bookings.html

    path('api/', include(router.urls)),
]