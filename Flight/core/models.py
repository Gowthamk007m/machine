from django.db import models


# Create your models here.



#Airport Filght routes model
class Airportroutes(models.Model):
    code = models.CharField(max_length=8,unique=True)

    def __str__(self):
        return self.code
    
class Connetion(models.Model):
    takeoff_code=models.ForeignKey(Airportroutes, on_delete=models.CASCADE)
    destination_code = models.ForeignKey(Airportroutes,related_name="destination_code", on_delete=models.CASCADE)
    position = models.IntegerField()
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.takeoff_code} to {self.destination_code}'
    

    
    