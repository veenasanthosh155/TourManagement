from django.db import models

# Create your models here.
class Package(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField()
    image=models.ImageField(upload_to="images/category" ,null=True,blank=True )
    def __str__(self):
        return self.name

class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_ph=models.CharField(max_length=12)
    name=models.ForeignKey(Package,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)
    def __str__(self):
        return f"{self.cus_name} - {self.name.name} - {self.booking_date}"

