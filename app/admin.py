from django.contrib import admin
from app.models import Person, MyModel, AdresUrl
# Register your models here.
admin.site.register(Person)
admin.site.register(MyModel)
admin.site.register(AdresUrl)