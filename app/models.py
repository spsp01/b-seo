from django.db import models
from .utils import generator_code, create


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')
    def __str__(self):
        return self.name

class MyModel(models.Model):
    someAttr = models.CharField(max_length=255)

    def __unicode__(self):
        return self.someAttr

    def natural_key(self):
        return self.my_natural_key

class ProjektUrl(models.Model):
    BRAND = (('PM', 'Wewnętrzny'), ('GM','GroupM'))

    projekt = models.CharField(verbose_name='Projekt Url', default='domain.com', max_length=255)
    active = models.BooleanField(default=True)
    brand = models.CharField(max_length=255, choices=BRAND, default='PM')
    account = models.CharField(max_length=255)
    budzet = models.IntegerField()
    image = models.FileField(upload_to='logo/',null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.projekt

class Url(models.Model):
    url = models.TextField(verbose_name='Url', default='http://domain.com/link1', max_length=2000)
    projekt = models.ForeignKey('ProjektUrl', on_delete=models.CASCADE)

    def __str__(self):
        return self.url

class UrlShortner(models.Model):
    url = models.CharField(max_length=255)
    shortcode = models.CharField(max_length=16, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.url
    
    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode=="":
            self.shortcode = create(self)
        super(UrlShortner, self).save(*args,**kwargs)