from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    LANDLORD = "landlord"
    CONTRACTOR = "contractor"

    ROLE_CHOICES = [
        (LANDLORD, "Landlord"),
        (CONTRACTOR, "Contractor"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"


class ContractorProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="contractor_profile"
    )
    specialty = models.CharField(max_length=100)
    postcode = models.CharField(max_length=20)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    is_available = models.BooleanField(default=True)

    rating = models.DecimalField(max_digits=3, decimal_places=2, default=5.0)

    def __str__(self):
        return f"Contractor: {self.user.get_full_name() or self.user.username} - {self.specialty}"


