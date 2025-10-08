# movie_theater_booking/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # API and HTML routes
    path('', include('bookings.urls')),
]

if settings.DEBUG:
    urlpatterns += static('/proxy/8000/media/', document_root=settings.MEDIA_ROOT)