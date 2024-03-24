from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Slide(models.Model):
    # Define the fields for your Slide model here
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='slides/')
    description = models.TextField()

    def __str__(self):
        return self.title