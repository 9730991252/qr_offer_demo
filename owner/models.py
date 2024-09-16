from django.db import models
import uuid  
# Create your models here.
class Office_employee(models.Model):
    name = models.CharField(max_length=1000)
    mobile = models.IntegerField()
    pin = models.IntegerField()
    status = models.IntegerField(default=1)


class Qr_code(models.Model):
    employee = models.ForeignKey(Office_employee,on_delete=models.PROTECT,null=True)
    tag_number = models.CharField(unique=True, max_length=100)
    scan_status = models.IntegerField(default=0)
    redeem_status = models.IntegerField(default=0)
    generate_date = models.DateTimeField(auto_now_add=True)
    date = models.DateField(auto_now_add=True)
    sr_num = models.IntegerField(null=True )