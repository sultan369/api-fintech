from django.test import TestCase
from datetime import datetime, timezone
from decimal import Decimal

from ..models import Loan, Payment


class LoanTest(TestCase):
    """ Test module for Loan and Payment model """
    
    def setUp(self):
        Loan.objects.create(
            amount=Decimal('1000.00'), term=12, rate=Decimal('0.05'), date_initial=datetime(2019,3,24,11,30).astimezone(tz=timezone.utc)
        )

    def test_loan(self):
        loan_01 = Loan.objects.get(amount=Decimal('1000.00'))
        self.assertEqual(
            loan_01.installment, Decimal('85.61')) #check use of decimals, because the digit is wrong
    
    def test_payment_made(self):
        loan_01 = Loan.objects.get(amount=Decimal('1000.00'))
        Payment.objects.create(
            loan_id=loan_01, type='MD', date=datetime(2019,4,24).astimezone(tz=timezone.utc), amount=Decimal('100')
        )
        payment = Payment.objects.get(type='MD')
        self.assertEqual(
            payment.amount, Decimal('100'))
    
    def test_payment_missed(self):
        loan_01 = Loan.objects.get(amount=Decimal('1000.00'))
        Payment.objects.create(
            loan_id=loan_01, type='MS', date=datetime(2019,4,24).astimezone(tz=timezone.utc), amount=Decimal('200')
        )
        payment = Payment.objects.get(type='MS')
        self.assertEqual(
            payment.amount, Decimal('200'))
    
    """
        This test should failure, because 0 is not a option type.
        Search a way to do this.
    """
    def test_payment_error(self):
        loan_01 = Loan.objects.get(amount=Decimal('1000.00'))
        Payment.objects.create(
            loan_id=loan_01, type='0', date=datetime(2019,4,24).astimezone(tz=timezone.utc), amount=Decimal('300')
        )
        payment = Payment.objects.get(type='0')
        self.assertEqual(
            payment.amount, Decimal('300'))


class BalanceTest(TestCase):
    """ Test module for Balance model """
    
    def setUp(self):
        self.loan_01 = Loan.objects.create(
            amount=Decimal('1000.00'), term=12, rate=Decimal('0.05'), date_initial=datetime(2019,3,24,11,30).astimezone(tz=timezone.utc)
        )
        Payment.objects.create(
            loan_id=self.loan_01, type='MD', date=datetime(2019,4,24).astimezone(tz=timezone.utc), amount=Decimal('200')
        )
        Payment.objects.create(
            loan_id=self.loan_01, type='MD', date=datetime(2019,4,24).astimezone(tz=timezone.utc), amount=Decimal('200')
        )
        Payment.objects.create(
            loan_id=self.loan_01, type='MS', date=datetime(2019,4,24).astimezone(tz=timezone.utc), amount=Decimal('200')
        )
    
    def test_balance_loan_valid(self):
        self.assertEqual(Loan.objects.get_balance(loan_id=self.loan_01.pk, date_base=datetime(2019,4,25).astimezone(tz=timezone.utc)), Decimal('600'))
    
    def test_balance_loan_invalid(self):
        self.assertEqual(Loan.objects.get_balance(0, date_base=datetime(2019,3,25).astimezone(tz=timezone.utc)), Decimal('0'))

    def test_balance_without_payments(self):
        self.assertEqual(Loan.objects.get_balance(loan_id=self.loan_01.pk, date_base=datetime(2019,3,25).astimezone(tz=timezone.utc)), self.loan_01.amount)
    
    def test_balance_loan_without_date_base(self):
        self.assertEqual(Loan.objects.get_balance(loan_id=self.loan_01.pk), Decimal('600'))