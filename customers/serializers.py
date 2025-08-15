from rest_framework import serializers
from .models import Customer

class CustomerRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'age', 'monthly_income', 'phone_number']

    def create(self, validated_data):
        monthly_income = validated_data['monthly_income']
        approved_limit = round((36 * monthly_income) / 100000) * 100000  # nearest lakh
        validated_data['approved_limit'] = approved_limit
        validated_data['current_debt'] = 0
        return Customer.objects.create(**validated_data)
