from django.db import models

# Create your models here.

class NewAiportModel(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class AirportConnections(models.Model):
    parent=models.ForeignKey(NewAiportModel, on_delete=models.CASCADE, related_name='connections',null=True)
    child_left=models.ForeignKey(NewAiportModel, on_delete=models.CASCADE, related_name='left_connections',blank=True,null=True)
    child_right=models.ForeignKey(NewAiportModel, on_delete=models.CASCADE, related_name='right_connections',blank=True,null=True)
    duration_left=models.IntegerField(help_text="Distance in km",blank=True,null=True)
    duration_right=models.IntegerField(help_text="Distance in km",blank=True,null=True)
    
    def __str__(self):
        return f"{self.parent} -> {self.child_left} ({self.duration_left} km) -> {self.child_right} ({self.duration_right} km)"
    
    