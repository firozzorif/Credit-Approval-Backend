from rest_framework import serializers
from .models import Loan

class CheckEligibilitySerializer(serializers.Serializer):
    """
    Serializer for checking loan eligibility.
    """
    customer_id = serializers.IntegerField()
    loan_amount = serializers.FloatField()
    interest_rate = serializers.FloatField()
    tenure = serializers.IntegerField()

    def validate(self, data):
        # Ensure positive values for loan_amount and tenure
        if data['loan_amount'] <= 0:
            raise serializers.ValidationError({"loan_amount": "Loan amount must be positive"})
        if data['tenure'] <= 0:
            raise serializers.ValidationError({"tenure": "Tenure must be positive"})
        if data['interest_rate'] < 0:
            raise serializers.ValidationError({"interest_rate": "Interest rate cannot be negative"})
        return data


class LoanSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing loan details.
    """
    class Meta:
        model = Loan
        fields = [
            'loan_id',
            'loan_amount',
            'tenure',
            'interest_rate',
            'monthly_repayment',
            'emis_paid_on_time',
            'start_date',
            'end_date',
            'customer'
        ]
