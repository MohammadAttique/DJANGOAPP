from django.db import models
from brands.models import Brand
from categories.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Discounted price if applicable"
    )
    stock_quantity = models.PositiveIntegerField()
    brand = models.ForeignKey(
        Brand,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='product_images/',
        null=True,
        blank=True,
        help_text="Upload an image for the product"
    )

    def formatted_price(self):
        if self.discounted_price is not None:
            discount_percentage = ((self.price - self.discounted_price) / self.price) * 100
            return f"Rs.{self.discounted_price:.2f} Rs.{self.price:.2f} {discount_percentage:.0f}% OFF"
        else:
            return f"Rs.{self.price:.2f}"

    def __str__(self):
        return self.name
