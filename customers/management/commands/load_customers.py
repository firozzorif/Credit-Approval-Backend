from django.core.management.base import BaseCommand
from customers.models import Customer
import pandas as pd
import os

class Command(BaseCommand):
    help = 'Load customer data from Excel (same folder as this script)'

    def handle(self, *args, **kwargs):
        # File is in the same directory as this .py file
        file_path = os.path.join(os.path.dirname(__file__), 'customer_data.xlsx')

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        df = pd.read_excel(file_path)

        for _, row in df.iterrows():
            Customer.objects.update_or_create(
                customer_id=row['Customer ID'],
                defaults={
                    'first_name': row['First Name'],
                    'last_name': row['Last Name'],
                    'age': row['Age'],
                    'phone_number': str(row['Phone Number']),
                    'monthly_income': row['Monthly Salary'],
                    'approved_limit': row['Approved Limit'],
                    'current_debt': 0  # Set default since not in Excel
                }
            )
        self.stdout.write(self.style.SUCCESS("Customer data loaded successfully"))
