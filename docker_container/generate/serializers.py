from rest_framework import serializers
from . models import Pizza


class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        # all Pizza model fields
        fields = '__all__'

# class ToppingSerializer(serializers.ModelSerializer):
#         class Meta:
#             model = Topping
#             # all Pizza model fields
#             fields = '__all__'
