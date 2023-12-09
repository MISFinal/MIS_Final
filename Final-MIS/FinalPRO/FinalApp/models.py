from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(verbose_name="Date of Birth")
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_available = models.IntegerField()
    serial_number = models.CharField(max_length=255)
    category = models.CharField(max_length=255, default='Default Category')
    review_comment = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def __str__(self):
        return f"Inventory for {self.product.name}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s Cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_quantity = models.IntegerField()

    def __str__(self):
        return f"{self.cart.user.username}'s Cart Item"

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_of_purchase = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderDetails(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order Detail {self.id} for Order {self.order.id}"

class Receipt(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    number_of_items = models.IntegerField()

    def __str__(self):
        return f"Receipt {self.id} for Order {self.order.id}"


class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name
