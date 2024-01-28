from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from brands.models import Brand
from categories.models import Category
from .models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        self.brand = Brand.objects.create(name='Test Brand')
        self.category = Category.objects.create(name='Test Category')
        self.product = Product.objects.create(
            name='Test Product',
            description='Product for testing',
            price=100.00,
            discounted_price=80.00,
            stock_quantity=10,
            brand=self.brand,
            category=self.category,
            image=SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        )

    # Test 1: Product creation
    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.description, 'Product for testing')
        self.assertEqual(self.product.price, 100.00)
        self.assertEqual(self.product.discounted_price, 80.00)
        self.assertEqual(self.product.stock_quantity, 10)
        self.assertEqual(self.product.brand, self.brand)
        self.assertEqual(self.product.category, self.category)

    # Test 2: Product formatted price with discount
    def test_product_formatted_price_with_discount(self):
        formatted_price = self.product.formatted_price()
        expected_price = "Rs.80.00 Rs.100.00 20% OFF"
        self.assertEqual(formatted_price, expected_price)

    # Test 3: Product formatted price without discount
    def test_product_formatted_price_without_discount(self):
        self.product.discounted_price = None
        formatted_price = self.product.formatted_price()
        expected_price = "Rs.100.00"
        self.assertEqual(formatted_price, expected_price)

    # Test 4: Product string representation
    def test_product_str_representation(self):
        expected_str = "Test Product"
        self.assertEqual(str(self.product), expected_str)

    # Test 5: Product image upload
    def test_product_image_upload(self):
        self.assertIsNotNone(self.product.image)
        self.assertIn("product_images", self.product.image.name)

    # Test 6: Product without brand and category
    def test_product_without_brand_and_category(self):
        product_without_brand_category = Product.objects.create(
            name='Product without Brand and Category',
            description='Product without brand and category for testing',
            price=50.00,
            stock_quantity=5,
        )
        self.assertIsNone(product_without_brand_category.brand)
        self.assertIsNone(product_without_brand_category.category)

    # Test 7: Product with null discounted price
    def test_product_with_null_discounted_price(self):
        product_with_null_discount = Product.objects.create(
            name='Product with Null Discount',
            description='Product with null discounted price for testing',
            price=75.00,
            stock_quantity=8,
            brand=self.brand,
            category=self.category,
            discounted_price=None,
        )
        formatted_price = product_with_null_discount.formatted_price()
        expected_price = "Rs.75.00"
        self.assertEqual(formatted_price, expected_price)

    # Test 8: Product without image
    def test_product_without_image(self):
        product_without_image = Product.objects.create(
            name='Product without Image',
            description='Product without image for testing',
            price=120.00,
            stock_quantity=15,
            brand=self.brand,
            category=self.category,
        )
       
