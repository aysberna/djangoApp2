from django.db import models

# Create your models here.
class Operation(models.Model):
    name = models.CharField(max_length=50)

class Bin(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    collection_frequency = models.IntegerField()
    last_collection = models.DateTimeField()

class Collection(models.Model):
    operation_id = models.ForeignKey(Operation, on_delete=models.CASCADE)
    bin_id = models.ForeignKey(Bin, on_delete=models.CASCADE)
    collection_time = models.DateTimeField()
