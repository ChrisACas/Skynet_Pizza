from django.db import models


# Create your models here.
class Pizza(models.Model):
    crust = models.CharField(max_length=80)
    sauce = models.CharField(max_length=80)
    cheese = models.CharField(max_length=80)

    def __str__(self):
        return self.crust.lower() + ' crust, ' + self.sauce + ' sauce, and ' + self.cheese + ' cheese'


class Topping(models.Model):
    pizza = models.ForeignKey(to=Pizza, on_delete=models.CASCADE)
    topping_type = models.CharField(max_length=80)
    ingredient = models.CharField(max_length=250)
    nutritional = models.CharField(max_length=250)

    def __str__(self):
        return self.topping_type + ' | ' + self.ingredient
