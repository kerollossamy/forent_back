from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    # property = models.ForeignKey(Property, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=255)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
