from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Booking
from datetime import date
from rest_framework.test import APITestCase
from rest_framework import status


# ----------------------------
# Unit Tests
# ----------------------------
class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Inception",
            description="A test movie.",
            release_date=date(2010, 7, 16),
            duration=148
        )

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Inception")


class SeatModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="For seat testing",
            release_date=date.today(),
            duration=100
        )
        self.seat = Seat.objects.create(movie=self.movie, row='A', number=1)

    def test_seat_str(self):
        self.assertIn("A1", str(self.seat))
        self.assertIn("Available", str(self.seat))


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="tester")
        self.movie = Movie.objects.create(
            title="Matrix",
            description="Sci-fi test",
            release_date=date(1999, 3, 31),
            duration=136
        )
        self.seat = Seat.objects.create(movie=self.movie, row='B', number=2)
        self.booking = Booking.objects.create(
            movie=self.movie, seat=self.seat, user=self.user
        )

    def test_booking_str(self):
        text = str(self.booking)
        self.assertIn("Matrix", text)
        self.assertIn("B2", text)


# ----------------------------
# API Tests
# ----------------------------
class APITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass123")
        self.client.login(username="testuser", password="pass123")

        self.movie = Movie.objects.create(
            title="Interstellar",
            description="Space test",
            release_date=date(2014, 11, 7),
            duration=169
        )

    def test_movie_list_api(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("Interstellar", str(response.data))

    def test_create_booking_api(self):
        seat = Seat.objects.create(movie=self.movie, row="C", number=5)
        response = self.client.post("/api/bookings/", {
            "movie": self.movie.id,
            "seat": seat.id
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_prevent_double_booking(self):
        seat = Seat.objects.create(movie=self.movie, row="D", number=1)
        Booking.objects.create(movie=self.movie, seat=seat, user=self.user)
        seat.is_booked = True
        seat.save()

        # Attempt to book again
        response = self.client.post("/api/bookings/", {
            "movie": self.movie.id,
            "seat": seat.id
        })

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("already booked", str(response.data).lower())
