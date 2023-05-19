from django.db import models




class Car(models.Model):
    car_owner = models.ForeignKey('dealer_users.User', name="User", on_delete=models.CASCADE, blank=True, null=True)
    car_model = models.CharField(max_length=200)
    milage = models.IntegerField(default=0)
    new = models.BooleanField(default=False)
    used = models.BooleanField(default=False)
    damaged = models.BooleanField(default=False)
    sell_info = models.ForeignKey("cars.SellInfo", name="SellInfo", on_delete=models.CASCADE, blank=True, null=True)



class SellInfo(models.Model):
    bot_by = models.CharField(max_length=200)
    date_bot = models.DateTimeField()