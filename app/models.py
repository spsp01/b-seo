from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, verbose_name='full name')

class MyModel(models.Model):
    someAttr = models.CharField(max_length=255)

    def __unicode__(self):
        return self.someAttr

    def natural_key(self):
        return self.my_natural_key