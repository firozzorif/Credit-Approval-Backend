from django.core.management.base import BaseCommand
from loans.models import Loan
from customers.models import Customer
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Load loan data from Excel (same folder as this script)'

    def handle(self, *args, **kwargs):
        # File is in the same directory as this .py file
        file_path = os.path.join(os.path.dirname(__file__), 'loan_data.xlsx')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            customer = Customer.objects.get(customer_id=row['Customer ID'])
            Loan.objects.update_or_create(
                loan_id=row['Loan ID'],
                defaults={
                    'customer': customer,
                    'loan_amount': row['Loan Amount'],
                    'tenure': row['Tenure'],
                    'interest_rate': row['Interest Rate'],
                    'monthly_repayment': row['Monthly payment'],
                    'emis_paid_on_time': row['EMIs paid on Time'],
                    'start_date': row['Date of Approval'],
                    'end_date': row['End Date']
                }
            )
        self.stdout.write(self.style.SUCCESS("Loan data loaded successfully"))
