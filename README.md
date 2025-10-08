# Movie Theater Booking System

Jess Movies is a Django-based web application that allows users to view available movies, select seats, and make bookings. It also includes API endpoints for movies, seats, and bookings, as well as deployment instructions for Render.

---

## Features

* View a list of movies with images and descriptions.
* Select seats for specific movies (each movie has its own seat map).
* Prevent double-booking of the same seat for a movie.
* Track previous bookings.
* REST API for movies, seats, and bookings.
* Local development using SQLite and deployment to Render using PostgreSQL.

---

## Technologies Used

* **Python 3.12**
* **Django 4.2.11**
* **Django REST Framework**
* **Gunicorn + Uvicorn** 
* **WhiteNoise**
* **SQLite (local)** / **PostgreSQL (Render)**

---

## Project Structure

```
movie_theater_booking/
├── bookings/
│   ├── migrations/
│   ├── templates/bookings/
│   │   ├── movies.html
│   │   ├── seats.html
│   │   └── previous_bookings.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│   └── tests.py
├── movie_theater_booking/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── media/movie_posters/
│   ├── la_la_land.jpg
│   ├── spirited_away.jpg
│   ├── spiderman_spiderverse.jpg
│   ├── corpse_bride.jpg
│   └── past_lives.jpg
├── staticfiles/
├── manage.py
├── requirements.txt
├── build.sh
└── Procfile
```

---

## Key Files Overview

### `models.py`

Defines three models:

* **Movie** — title, description, release date, duration, image.
* **Seat** — linked to a movie, contains row (A–E), number (1–10), and booking status.
* **Booking** — connects a user, movie, and seat.

### `views.py`

Contains both Django template views and REST API viewsets:

* `movie_list` → displays all movies.
* `seat_booking` → shows available seats and handles booking submissions.
* `booking_history` → shows user bookings.
* API viewsets (`MovieViewSet`, `SeatViewSet`, `BookingViewSet`).

### `urls.py`

Defines app-level routes for movie listing, seat booking, and booking history.

### `settings.py`

* Uses **SQLite locally** and **PostgreSQL on Render**.
* Serves static and media files via WhiteNoise.

### `tests.py`

Unit tests for models and API endpoints:

* Tests string representations.
* Validates seat double-booking prevention.
* Confirms API endpoints return correct responses.

---

## Local Testing and Development

### Step 1: Create and Activate Virtual Environment

```bash
python3 -m venv myenv
source myenv/bin/activate
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Run Migrations

```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

### Step 4: Create Superuser

```bash
python3 manage.py createsuperuser
```

### Step 5: Run Development Server

```bash
python3 manage.py runserver 0.0.0.0:3000
```

Visit: `http://127.0.0.1:3000` or `https://app-<username>-<id>.devedu.io/`

## Example Movie Data

You can manually create movies through the admin panel or Django shell:

```bash
python manage.py shell
```

```python
from bookings.models import Movie
Movie.objects.create(title='La La Land', description='A jazz pianist falls for an aspiring actress.', release_date='2016-12-09', duration=128)
```

To populate seats automatically:

```python
from bookings.models import Movie, Seat
rows = ['A', 'B', 'C', 'D', 'E']
for movie in Movie.objects.all():
    for r in rows:
        for n in range(1, 11):
            Seat.objects.get_or_create(movie=movie, row=r, number=n)
```

---

## Notes

* Use **SQLite** locally (no need for PostgreSQL service).
* Render automatically provides **PostgreSQL** and `DATABASE_URL`.
* If you see `OperationalError: connection refused`, you’re likely trying to use PostgreSQL locally.

---

## Tests

Run all unit and API tests:

```bash
python3 manage.py test
```

##AI Statement

This project incorporated limited AI assistance through ChatGPT (OpenAI, GPT-5) to support development and documentation. ChatGPT was used strictly as an educational aid and productivity enhancer, not as a substitute for human understanding or authorship.

**How ChatGPT Was Used**

Project Planning: Helped outline the Django setup process, database structure, and workflow organization.

Code Guidance: Provided suggestions for model relationships, REST API configuration, and template logic corrections.

Debugging Assistance: Offered explanations and step-by-step resolutions for common Django and deployment errors.

Documentation: Assisted in structuring and editing this README file to ensure clarity, technical accuracy, and consistency in style.

**Ethical Use and Verification**

All AI-generated outputs were reviewed, tested, and manually modified by the developer. ChatGPT’s role was on explaining concepts and improving efficiency. Every piece of final code, configuration, and documentation was written or verified by the human author in accordance with academic integrity standards.


Developed for **CS4300 Homework 2** — Django Movie Theater Booking System.
