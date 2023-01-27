from django.contrib import admin
from .models import Choroby, Lekarze, Pacjenci, sf36_raw, sf36_recoded

admin.site.register(Choroby)
admin.site.register(Lekarze)
admin.site.register(Pacjenci)
admin.site.register(sf36_raw)
admin.site.register(sf36_recoded)