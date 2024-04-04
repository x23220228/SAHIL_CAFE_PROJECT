from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            try:
                img = Image.open(self.image.path)
                output_size = (400, 300)  # Adjust these dimensions as needed
                img.thumbnail(output_size)
                img.save(self.image.path)
            except OSError:
                # Handle the case where the uploaded file is not a valid image
                pass
    
    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)