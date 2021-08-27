from django.db import models
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=50)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, default=None)
    zip_code = models.CharField(max_length=10, default=None)
    balance = models.IntegerField(max_length=50, blank=True, default=None)
    weekly_pickup_day = models.CharField(max_length=50, default=None)
    one_time_pickup = models.DateField(max_length=50, blank = True, default=None)
    suspend_start = models.DateField(max_length=50, blank = True, default=None)
    suspend_end = models.DateField(max_length=50, blank = True, default=None)

    def __str__(self):
        return self.name
