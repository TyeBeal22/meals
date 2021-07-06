from django.db import models
from django.utils.text import slugify
from datetime import datetime
import random
import uuid
from meals.models import Meals

class Order(models.Model):
  meal = models.CharField(max_length=200)
  name = models.CharField(max_length=200)
  meal_id = models.CharField(max_length=10,blank=True)
  email = models.CharField(max_length=100)
  phone = models.CharField(max_length=100)
  message = models.TextField(blank=True)  
  guests = models.IntegerField(default=0) 
  contact_date = models.DateTimeField(default=datetime.now)
  delivery_address = models.TextField(blank=True, null=True)
  is_delivery = models.BooleanField(default=True)
  event_date = models.CharField(max_length=100)

  def __str__(self):
    return self.name




class MyUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)