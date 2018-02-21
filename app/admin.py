from django.contrib import admin
from app.models import Person, MyModel, ProjektUrl, Url, UrlShortner
# Register your models here.
admin.site.register(Person)
admin.site.register(MyModel)
admin.site.register(ProjektUrl)
admin.site.register(Url)
admin.site.register(UrlShortner)