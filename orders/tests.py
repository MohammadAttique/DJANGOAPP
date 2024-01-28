from django.test import TestCase
from accounts.models import CustomUser
from shop.models import Product
from .models import Order, OrderDetail, Cart

class OrderModelsTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(username='testuser', password='testpassword')
        self.product = Product.objects.create(
            name='Test Product',
            description='Product for testing',
            price=100.00,
            stock_quantity=10
        )
        self.order = Order.objects.create(
            user=self.user,
            total_amount=150.00
        )
        self.order_detail = OrderDetail.objects.create(
            order=self.order,
            product=self.product,
            quantity=2,
            subtotal=200.00
        )
        self.cart_item = Cart.objects.create(
            user=self.user,
            product=self.product,
            quantity=3
        )

    # Test 1: Order creation
    def test_order_creation(self):
        self.assertEqual(self.order.user, self.user)
        self.assertEqual(self.order.total_amount, 150.00)

    # Test 2: OrderDetail creation
    def test_order_detail_creation(self):
        self.assertEqual(self.order_detail.order, self.order)
        self.assertEqual(self.order_detail.product, self.product)
        self.assertEqual(self.order_detail.quantity, 2)
        self.assertEqual(self.order_detail.subtotal, 200.00)

    # Test 3: Cart creation
    def test_cart_creation(self):
        self.assertEqual(self.cart_item.user, self.user)
        self.assertEqual(self.cart_item.product, self.product)
        self.assertEqual(self.cart_item.quantity, 3)

    # Test 4: Order string representation
    def test_order_string_representation(self):
        expected_str = f"Order {self.order.id} - {self.user.username}"
        self.assertEqual(str(self.order), expected_str)



    # Test 5: OrderDetail subtotal calculation
    def test_order_detail_subtotal_calculation(self):
        expected_subtotal = self.order_detail.product.price * self.order_detail.quantity
        self.assertEqual(self.order_detail.subtotal, expected_subtotal)

    # Test 6: Cart item quantity update
    def test_cart_item_quantity_update(self):
        new_quantity = 5
        self.cart_item.quantity = new_quantity
        self.cart_item.save()
        self.assertEqual(Cart.objects.get(id=self.cart_item.id).quantity, new_quantity)

    