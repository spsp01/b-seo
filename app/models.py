from django.db import models

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
    projekt = models.TextField(verbose_name='Projekt Url', default='domain.com', max_length=2000)

    def __str__(self):
        return self.projekt

class Url(models.Model):
    url = models.TextField(verbose_name='Url', default='http://domain.com/link1', max_length=2000)
    projekt = models.ForeignKey('ProjektUrl', on_delete=models.CASCADE)

    def __str__(self):
        return self.url