from django.db import models
from django.contrib.auth.models import User


# Create your models here
class Pizza(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True)
    crust = models.CharField(max_length=80)
    sauce = models.CharField(max_length=80)
    cheese = models.CharField(max_length=80)

    def __str__(self):
        return self.crust + ' crust | ' + self.sauce + ' sauce | ' + self.cheese + ' cheese'


class Topping(models.Model):
    pizza = models.ForeignKey(to=Pizza, on_delete=models.CASCADE)
    topping = models.CharField(max_length=80)
    

    def __str__(self):
        return self.topping
