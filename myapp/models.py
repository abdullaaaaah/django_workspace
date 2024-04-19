# Create your models here.
from django.db import models
from datetime import datetime
import requests

class UWBRead(models.Model):
    timestamp_utc = models.DateTimeField()
    device_uid = models.CharField(max_length=100)
    manufacturer_name = models.CharField(max_length=100)
    distance = models.IntegerField()
    count = models.IntegerField()

class UWBData(models.Model):
    transmitter_serial_number = models.CharField(max_length=100)
    node_type = models.CharField(max_length=100)
    all_count = models.IntegerField()

    @classmethod
    def fetch_and_create_data(cls):
        # Fetch data from UWB Gateway API
        url = 'http://uwb.axionics.tech/api/tag/upload/'  # Replace with correct API
        response = requests.get(url)

        if response.status_code == 200:
            json_data = response.json()
            
            # Extract UWBData fields from the JSON data
            uwb_data = cls.objects.create(
                transmitter_serial_number=json_data['transmitterSerialNumber'],
                node_type=json_data['nodeType'],
                all_count=json_data['allCount']
            )

            # Extract UWBReads from the JSON data
            for read_data in json_data['reads']:
                UWBRead.objects.create(
                    uwb_data=uwb_data,
                    timestamp_utc=cls.convert_to_datetime(read_data['timeStampUTC']),
                    device_uid=read_data['deviceUID'],
                    manufacturer_name=read_data['manufacturerName'],
                    distance=read_data['distance'],
                    count=read_data['count']
                )

    @staticmethod
    def convert_to_datetime(timestamp_str):
        # Convert timestamp string to datetime object
        return datetime.fromtimestamp(timestamp_str)


'''
from django.db import models
import requests

class UWBData(models.Model):
    # Define fields to store UWB data
    transmitter_serial_number = models.CharField(max_length=100)
    node_type = models.CharField(max_length=100)
    node_serial_number = models.CharField(max_length=100)
    timestamp_utc = models.DateTimeField()
    device_uid = models.CharField(max_length=100)
    manufacturer_name = models.CharField(max_length=100)

    @classmethod
    def fetch_and_create_data(cls):
        # Fetch data from UWB Gateway API
        url = 'http://uwb.axionics.tech/api/tag/upload/'  # Replace with correct API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            # Extract relevant data and create UWBData objects
            for read in data['reads']:
                uwb_data = cls.objects.create(
                    transmitter_serial_number=data['transmitterSerialNumber'],
                    node_type=data['nodeType'],
                    node_serial_number=data['nodeSerialNumber'],
                    timestamp_utc=read['timeStampUTC'],
                    device_uid=read['deviceUID'],
                    manufacturer_name=read['manufacturerName'],
                    rssi=read.get('rssi', 0)  # Assuming 'rssi' is present in the data
                )
                uwb_data.save()
'''