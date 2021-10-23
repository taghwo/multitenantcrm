from django.db import models
from django.utils.timezone import now
class Feedback(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(blank=True, null=True)
    phonenumber = models.CharField(blank=True, null=True, max_length=15)
    message = models.TextField(max_length=3000)
    created_at = models.DateTimeField(auto_now_add=now)

    class meta:
        verbose_name_plural = ['feedback']

    def __str__(self) -> str:
        return self.name