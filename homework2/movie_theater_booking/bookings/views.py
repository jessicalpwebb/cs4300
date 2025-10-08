from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# ----------------------------
# Django REST Framework ViewSets
# ----------------------------
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        movie_id = request.data.get('movie')
        seat_id = request.data.get('seat')

        try:
            seat = Seat.objects.get(id=seat_id)
            if seat.is_booked:
                return Response({'error': 'Seat already booked!'}, status=status.HTTP_400_BAD_REQUEST)

            booking = Booking.objects.create(
                movie_id=movie_id,
                seat=seat,
                user=request.user if request.user.is_authenticated else None,
            )
            seat.is_booked = True
            seat.save()

            serializer = self.get_serializer(booking)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Seat.DoesNotExist:
            return Response({'error': 'Seat not found.'}, status=status.HTTP_404_NOT_FOUND)

# ----------------------------
# Regular Django Views (HTML templates)
# ----------------------------
def movie_list(request):
    """Display list of movies"""
    movies = Movie.objects.all()
    return render(request, 'bookings/movies.html', {'movies': movies})

def seat_booking(request, movie_id):
    """Display available seats for a movie and handle booking"""
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.filter(movie=movie)

    if request.method == "POST":
        seat_id = request.POST.get("seat_id")
        seat = get_object_or_404(Seat, id=seat_id, movie=movie)

        if seat.is_booked:
            messages.error(request, "That seat is already booked.")
        else:
            booking = Booking.objects.create(
                movie=movie,
                seat=seat,
                user=request.user if request.user.is_authenticated else None
            )
            seat.is_booked = True
            seat.save()
            messages.success(request, f"You booked seat {seat.row}{seat.number} for {movie.title}!")


            # Redirect
            return redirect('movie_list')

    return render(request, 'bookings/seats.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    """Display previous bookings"""
    bookings = Booking.objects.all()
    return render(request, 'bookings/previous_bookings.html', {'bookings': bookings})