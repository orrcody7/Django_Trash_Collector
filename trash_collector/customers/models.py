from django.db import models
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, default=None)
    zip_code = models.CharField(max_length=10, default=None)
    balance = models.IntegerField(blank=True, default=None, null=True)
    weekly_pickup_day = models.CharField(max_length=50, default=None)
    one_time_pickup = models.DateField(max_length=50, blank = True, default=None, null=True)
    suspend_start = models.DateField(max_length=50, blank = True, default=None, null=True)
    suspend_end = models.DateField(max_length=50, blank = True, default=None, null=True)

    def __str__(self):
        return self.name
    