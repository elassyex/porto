from django.db import models

class Ips(models.Model):
    ip = models.CharField(max_length=100)
    dev = models.TextField(max_length=24)
    browser = models.CharField(max_length=29)
    so = models.CharField(max_length=80)
    city = models.CharField(max_length=30, null=True)
    region = models.CharField(max_length=30,  null=True)
    country = models.CharField(max_length=30,  null=True)

    def __str__(self):
        return self.ip
        
