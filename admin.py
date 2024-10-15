from django.contrib import admin
from Sagamdharamshala.models import Sagamdharamshala
class SagamdharamshalAdmin(admin.ModelAdmin):
    list_diaplay = ('name','address','phoneno','roomno','amount','filetp')
admin.site.register(Sagamdharamshala, SagamdharamshalAdmin)

# Register your models here.
