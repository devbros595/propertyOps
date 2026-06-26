from django.db import models
from django.conf import settings


class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="services/")

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("paid", "Paid"),
        ("assigned", "Assigned"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]

    landlord = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="orders"
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    assigned_contractor = models.ForeignKey(
        "users.ContractorProfile",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="jobs",
    )
    property_address = models.TextField()
    postcode = models.CharField(max_length=12)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id} - {self.service.name} ({self.status})"


class Payment(models.Model):
    order = models.OneToOneField(
        Order, on_delete=models.CASCADE, related_name="payment_details"
    )
    stripe_payment_intent = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class ContractorPayout(models.Model):
    contractor = models.ForeignKey(
        "users.ContractorProfile", on_delete=models.CASCADE, related_name="payouts"
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    stripe_transfer_id = models.CharField(max_length=255, blank=True, null=True)
    paid = models.BooleanField(default=False)
    processed_at = models.DateTimeField(auto_now=True)
