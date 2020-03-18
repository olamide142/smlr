import uuid
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
import random
def randomId():
    characters = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in range(7):
        result += characters[random.randrange(len(characters))]
    return result

class SmlrUrl(models.Model):
    smlr_url_id = models.CharField(max_length=500, null=True, blank=True)
    owner = models.CharField(max_length=20, null=True, blank=True)
    destination_url = models.CharField(max_length=500, null=True)
    visits = models.BigIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return str(self.owner) +'-'+ str(self.smlr_url_id)


class Stat(models.Model):
    url = models.CharField(max_length=500, null=True, blank=True)
    date_visited = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return str(self.url.smrl_url) +'-'+ str(self.date_visited) 


