from django.db import models
class Sagamdharamshala(models.Model):
    name = models.CharField(max_length= 200)
    address = models.TextField()
    phoneno = models.IntegerField()
    roomno = models.IntegerField()
    amount = models.IntegerField()
    filetp = models.FileField(upload_to= 'Sagamdharamshala/', max_length= 250, null= True, default= None)
# Create your models here.
