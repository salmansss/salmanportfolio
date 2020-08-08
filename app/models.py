from django.db import models

# Create your models here.
class contactform(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    description = models.TextField()

    def __str__(self):
        return self.name




