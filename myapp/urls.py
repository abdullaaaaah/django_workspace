# myapp/urls.py
from django.urls import path
from .views import index, page_a, page_b, page_c, fetch_uwb_data#, get_distance_measurements
#from . import views  # Import the views module from the current directory

urlpatterns = [
    path('', index, name='index'),  # This pattern maps the root URL to the index view
    path('page_a/', page_a, name='page_a'),
    path('page_b/', page_b, name='page_b'),
    path('page_c/', page_c, name='page_c'),
    path('api/tag/upload/', fetch_uwb_data, name='fetch_uwb_data'),  # Add this pattern
    #path('api/get-distance-measurements/', get_distance_measurements, name='get_distance_measurements'),
]
