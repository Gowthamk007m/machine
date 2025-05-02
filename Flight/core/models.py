from django.db import models


# Create your models here.



#Airport Filght routes model
class Airportroutes(models.Model):
    code = models.CharField(max_length=8)

    def __str__(self):
        return self.code
    
class Connetion(models.Model):
    node=models.OneToOneField(Airportroutes, on_delete=models.CASCADE)
    current_code = models.CharField(max_length=8,unique=True)
    position = models.IntegerField()
    duration = models.IntegerField()
    
    new_code=Airportroutes(code=current_code)
    new_code.save()

    
    def __str__(self):
        return self.current_code