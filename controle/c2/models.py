from django.db import models

# Create your models here.

#Id Title,Latitude,Longitude,Icon, ip, mac
# 1 car1,-29.6197,-55.3795,2

class Dispositivo(models.Model):
  RED_TANK = '1'
  BLUE_TANK = '2'
  SENSOR = '3'
  UAV = '4'
  BLUE_SOLDIER = '5'
  RED_SOLDIER = '6'

  ICON_CHOICES = (
    (RED_TANK, 'red_tank'),
    (BLUE_TANK, 'blue_tank'),
    (SENSOR, 'sensor'),
    (UAV, 'uav'),
    (BLUE_SOLDIER, 'blue_soldier'),
    (RED_SOLDIER, 'red_soldier'),
  )

  title = models.CharField(
    max_length=10,
    null=False,
    blank=False
  )

  latitude = models.CharField(
    max_length=14,
    null=False,
    blank=False
  )

  longitude = models.CharField(
    max_length=14,
    null=False,
    blank=False
  )

  icon = models.CharField(
    choices=ICON_CHOICES,
    max_length=14,
    null=False,
    blank=False
  )

  ip = models.CharField(
    max_length=15,
    null=True,
    blank=True
  )

  mac = models.CharField(
    max_length=17,
     null=True,
    blank=True
  )

  pub_date = models.DateTimeField('date published'
  )  

  
  def __str__(self):
      return self.title
  
