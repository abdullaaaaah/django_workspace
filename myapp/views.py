# myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from .models import UWBData
from django.http import JsonResponse
import requests

def index(request):
    return render(request, 'index.html')

def page_a(request):
    return render(request, 'page_a.html')

def page_b(request):
    return render(request, 'page_b.html')

def page_c(request):
    return render(request, 'page_c.html')

def fetch_uwb_data(request):
    UWBData.fetch_and_create_data()
    return HttpResponse("UWB data fetched and created successfully!")


def chart_page(request):
    # Retrieve data from the database or another source
    # For demonstration purposes, let's assume data is a list of dictionaries
    data = [
        {'site_number': 'Site1', 'number_of_assets': 10},
        {'site_number': 'Site2', 'number_of_assets': 20},
        {'site_number': 'Site3', 'number_of_assets': 15},
        # Add more data as needed
    ]

    # Pass data to the template
    return render(request, 'page_a.html', {'data': data})


'''
def get_distance_measurements(request):
    # Logic to fetch distance measurements from your backend or database
    distance_measurements = {'xDistance': 100, 'yDistance': 500}  # Example data

    # Return the distance measurements as a JSON response
    return JsonResponse(distance_measurements)


def get_distance_measurements(request):
    try:
        # Fetch distance measurements from the UWB gateway or backend
        response = requests.get('http://uwb.axionics.tech/api/tag/upload/')
        data = response.json()
        
        # Extract xDistance and yDistance from the data (adjust as per your API response structure)
        x_distance = data.get('xDistance')
        y_distance = data.get('yDistance')
        
        # Return the distance measurements as a JSON response
        return JsonResponse({'xDistance': x_distance, 'yDistance': y_distance})
    except Exception as e:
        # Handle any errors that occur during the request or processing
        return JsonResponse({'error': str(e)}, status=500)

'''