"""
URL configuration for credit_approval project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from customers.views import RegisterCustomer
from loans.views import CheckEligibility, CreateLoan, ViewLoan, ViewLoansByCustomer

def api_home(request):
    return JsonResponse({
        'message': 'Credit Approval System API',
        'endpoints': {
            'register': '/register',
            'check_eligibility': '/check-eligibility', 
            'create_loan': '/create-loan',
            'view_loan': '/view-loan/<loan_id>',
            'view_loans_by_customer': '/view-loans/<customer_id>',
            'admin': '/admin/'
        }
    })

urlpatterns = [
    path('', api_home, name='home'),
    path('admin/', admin.site.urls),
    path('register', RegisterCustomer.as_view()),
    path('check-eligibility', CheckEligibility.as_view()),
    path('create-loan', CreateLoan.as_view()),
    path('view-loan/<int:loan_id>', ViewLoan.as_view()),
    path('view-loans/<int:customer_id>', ViewLoansByCustomer.as_view()),
]