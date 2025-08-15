from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from customers.models import Customer
from .models import Loan
from .serializers import CheckEligibilitySerializer
from .utils import calculate_emi, calculate_credit_score
from datetime import date, timedelta

# --------------------------
# 1. /check-eligibility
# --------------------------
class CheckEligibility(APIView):
    def post(self, request):
        serializer = CheckEligibilitySerializer(data=request.data)
        if serializer.is_valid():
            customer_id = serializer.validated_data['customer_id']
            loan_amount = serializer.validated_data['loan_amount']
            interest_rate = serializer.validated_data['interest_rate']
            tenure = serializer.validated_data['tenure']

            try:
                customer = Customer.objects.get(customer_id=customer_id)
            except Customer.DoesNotExist:
                return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

            credit_score = calculate_credit_score(customer)
            approval = False
            corrected_interest_rate = interest_rate

            # Calculate monthly installment for EMI check
            monthly_installment = calculate_emi(loan_amount, corrected_interest_rate, tenure)
            
            # Check if sum of EMIs > 50% of salary
            current_emis = sum(loan.monthly_repayment for loan in customer.loans.all())
            total_emis = current_emis + monthly_installment
            
            if total_emis > (customer.monthly_income * 0.5):
                approval = False
                return Response({
                    "customer_id": customer_id,
                    "approval": False,
                    "interest_rate": interest_rate,
                    "corrected_interest_rate": corrected_interest_rate,
                    "tenure": tenure,
                    "monthly_installment": monthly_installment
                })

            # Approval rules
            if credit_score > 50:
                approval = True
            elif 30 < credit_score <= 50:
                if interest_rate >= 12:
                    approval = True
                else:
                    corrected_interest_rate = 12
                    monthly_installment = calculate_emi(loan_amount, corrected_interest_rate, tenure)
            elif 10 < credit_score <= 30:
                if interest_rate >= 16:
                    approval = True
                else:
                    corrected_interest_rate = 16
                    monthly_installment = calculate_emi(loan_amount, corrected_interest_rate, tenure)
            else:  # credit_score <= 10
                approval = False

            return Response({
                "customer_id": customer_id,
                "approval": approval,
                "interest_rate": interest_rate,
                "corrected_interest_rate": corrected_interest_rate,
                "tenure": tenure,
                "monthly_installment": monthly_installment
            })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------
# 2. /create-loan
# --------------------------
class CreateLoan(APIView):
    def post(self, request):
        serializer = CheckEligibilitySerializer(data=request.data)
        if serializer.is_valid():
            customer_id = serializer.validated_data['customer_id']
            loan_amount = serializer.validated_data['loan_amount']
            interest_rate = serializer.validated_data['interest_rate']
            tenure = serializer.validated_data['tenure']

            try:
                customer = Customer.objects.get(customer_id=customer_id)
            except Customer.DoesNotExist:
                return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

            credit_score = calculate_credit_score(customer)
            approval = False
            corrected_interest_rate = interest_rate

            # Calculate monthly installment for EMI check
            monthly_installment = calculate_emi(loan_amount, corrected_interest_rate, tenure)
            
            # Check if sum of EMIs > 50% of salary
            current_emis = sum(loan.monthly_repayment for loan in customer.loans.all())
            total_emis = current_emis + monthly_installment
            
            if total_emis > (customer.monthly_income * 0.5):
                return Response({
                    "loan_id": None,
                    "customer_id": customer.customer_id,
                    "loan_approved": False,
                    "message": "Loan not approved - EMIs exceed 50% of monthly income",
                    "monthly_installment": monthly_installment
                })

            # Approval rules
            if credit_score > 50:
                approval = True
            elif 30 < credit_score <= 50:
                if interest_rate >= 12:
                    approval = True
                else:
                    corrected_interest_rate = 12
                    monthly_installment = calculate_emi(loan_amount, corrected_interest_rate, tenure)
            elif 10 < credit_score <= 30:
                if interest_rate >= 16:
                    approval = True
                else:
                    corrected_interest_rate = 16
                    monthly_installment = calculate_emi(loan_amount, corrected_interest_rate, tenure)
            else:  # credit_score <= 10
                approval = False

            if approval:
                start_date = date.today()
                end_date = start_date + timedelta(days=30 * tenure)

                loan = Loan.objects.create(
                    customer=customer,
                    loan_amount=loan_amount,
                    tenure=tenure,
                    interest_rate=corrected_interest_rate,
                    monthly_repayment=monthly_installment,
                    emis_paid_on_time=0,
                    start_date=start_date,
                    end_date=end_date
                )

                return Response({
                    "loan_id": loan.loan_id,
                    "customer_id": customer.customer_id,
                    "loan_approved": True,
                    "message": "Loan approved successfully",
                    "monthly_installment": monthly_installment
                })
            else:
                return Response({
                    "loan_id": None,
                    "customer_id": customer.customer_id,
                    "loan_approved": False,
                    "message": "Loan not approved based on credit score",
                    "monthly_installment": monthly_installment
                })

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# --------------------------
# 3. /view-loan/<loan_id>
# --------------------------
class ViewLoan(APIView):
    def get(self, request, loan_id):
        try:
            loan = Loan.objects.get(loan_id=loan_id)
        except Loan.DoesNotExist:
            return Response({"error": "Loan not found"}, status=status.HTTP_404_NOT_FOUND)

        customer = loan.customer
        return Response({
            "loan_id": loan.loan_id,
            "customer": {
                "id": customer.customer_id,
                "first_name": customer.first_name,
                "last_name": customer.last_name,
                "phone_number": customer.phone_number,
                "age": customer.age
            },
            "loan_amount": loan.loan_amount,
            "interest_rate": loan.interest_rate,
            "monthly_installment": loan.monthly_repayment,
            "tenure": loan.tenure
        })

# --------------------------
# 4. /view-loans/<customer_id>
# --------------------------
class ViewLoansByCustomer(APIView):
    def get(self, request, customer_id):
        loans = Loan.objects.filter(customer__customer_id=customer_id)
        if not loans.exists():
            return Response({"error": "No loans found for this customer"}, status=status.HTTP_404_NOT_FOUND)

        loan_list = []
        for loan in loans:
            repayments_left = loan.tenure - loan.emis_paid_on_time
            loan_list.append({
                "loan_id": loan.loan_id,
                "loan_amount": loan.loan_amount,
                "interest_rate": loan.interest_rate,
                "monthly_installment": loan.monthly_repayment,
                "repayments_left": repayments_left
            })
        return Response(loan_list)
