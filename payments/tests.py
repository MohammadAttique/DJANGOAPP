from django.test import TestCase
from accounts.models import CustomUser
from orders.models import Order
from .models import Payment, Invoice

class PaymentAndInvoiceModelsTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser', password='testpassword')
        self.order = Order.objects.create(user=self.user, total_amount=150.00)

    # Test 1: Payment creation
    def test_payment_creation(self):
        payment = Payment.objects.create(user=self.user, amount=50.00, success=True)
        self.assertEqual(payment.user, self.user)
        self.assertEqual(payment.amount, 50.00)
        self.assertTrue(payment.success)

    # Test 2: Invoice creation
    def test_invoice_creation(self):
        payment = Payment.objects.create(user=self.user, amount=50.00, success=True)
        invoice = Invoice.objects.create(order=self.order, amount=50.00, payment=payment)
        self.assertEqual(invoice.order, self.order)
        self.assertEqual(invoice.amount, 50.00)
        self.assertEqual(invoice.payment, payment)

    # Test 3: Payment and Invoice relationship
    def test_payment_and_invoice_relationship(self):
        payment = Payment.objects.create(user=self.user, amount=50.00, success=True)
        invoice = Invoice.objects.create(order=self.order, amount=50.00, payment=payment)
        self.assertEqual(payment.invoice_set.first(), invoice)

    # Test 4: Payment default value for success
    def test_payment_default_success_value(self):
        payment = Payment.objects.create(user=self.user, amount=50.00)
        self.assertFalse(payment.success)

    # Test 5: Invoice default value for payment
    def test_invoice_default_payment_value(self):
        invoice = Invoice.objects.create(order=self.order, amount=50.00)
        self.assertIsNone(invoice.payment)
