from datetime import date
from .models import Loan

def calculate_emi(principal, annual_rate, tenure_months):
    """
    Calculates the monthly EMI using compound interest formula.
    principal: Loan amount
    annual_rate: Annual interest rate (percentage)
    tenure_months: Number of months
    """
    if annual_rate == 0:  # No interest case
        return round(principal / tenure_months, 2)

    monthly_rate = annual_rate / 12 / 100
    emi = principal * monthly_rate * (1 + monthly_rate) ** tenure_months / ((1 + monthly_rate) ** tenure_months - 1)
    return round(emi, 2)


def calculate_credit_score(customer):
    """
    Calculates credit score out of 100 based on loan history.
    Rules from assignment:
    - Past loans paid on time → increases score
    - More past loans → decreases score
    - Loan activity in current year → decreases score
    - If total current loans > approved limit → score = 0
    """
    loans = Loan.objects.filter(customer=customer)
    score = 100  # base score

    # 1. Past loans paid on time
    on_time_loans = sum(1 for loan in loans if loan.emis_paid_on_time >= loan.tenure)
    score += on_time_loans * 5

    # 2. Number of past loans
    if loans.count() > 5:
        score -= 10

    # 3. Loan activity in current year
    current_year_loans = loans.filter(start_date__year=date.today().year).count()
    score -= current_year_loans * 2

    # 4. Loan approved volume
    total_loan_amount = sum(loan.loan_amount for loan in loans)
    if total_loan_amount > customer.approved_limit:
        return 0

    # Clamp score to range 0–100
    return max(0, min(100, score))
