from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



class User(models.Model):
    USER_ROLES = [
        ("owner", "Owner"),
        ("renter", "Renter"),
    ]
    username = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=7, choices=USER_ROLES)
    validation_states = models.BooleanField(default=False)
    registration_date = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField(
        upload_to="static/profile_pictures/",
        default= "static/images/blank_profile.png"
    )
    phone_number = PhoneNumberField(region="EG", blank=True, null=True)

    def __str__(self):
        return self.username
