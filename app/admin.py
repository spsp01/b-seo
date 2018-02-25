from django.contrib import admin
from app.models import Person, MyModel, ProjektUrl, Url, UrlShortner, UrlGSC
# Register your models here.
admin.site.register(Person)
admin.site.register(MyModel)
admin.site.register(ProjektUrl)
admin.site.register(Url)
admin.site.register(UrlShortner)
admin.site.register(UrlGSC)