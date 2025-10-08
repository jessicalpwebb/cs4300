from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    duration = models.IntegerField(help_text="Duration in minutes")
    image = models.ImageField(upload_to='movie_posters/', null=True, blank=True)
    def __str__(self):
        return self.title


class Seat(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="seats")
    row = models.CharField(default="A",max_length=1, help_text="Row letter, e.g. A, B, C")
    number = models.PositiveIntegerField(default=1,help_text="Seat number within the row")
    is_booked = models.BooleanField(default=False)

    class Meta:
        unique_together = ('movie', 'row', 'number')
        ordering = ['movie', 'row', 'number']

    def __str__(self):
        return f"{self.movie.title}: {self.row}{self.number} - {'Booked' if self.is_booked else 'Available'}"



class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    booking_date = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
        #return f"{self.user.username} - {self.movie.title} ({self.seat.seat_number})"

    def __str__(self):
        username = self.user.username if self.user else "Guest"
        return f"{username} - {self.movie.title} ({self.seat.row}{self.seat.number})"
