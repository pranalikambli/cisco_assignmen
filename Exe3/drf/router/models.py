from django.db import models

class RouterInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    sapid = models.CharField(max_length=18)
    hostname = models.CharField(max_length=14)
    loopback = models.GenericIPAddressField(protocol='IPv4')
    mac_address = models.CharField(max_length=17)
    is_active = models.BooleanField(default=True)

