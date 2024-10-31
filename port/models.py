from django.db import models

# Create your models here.
    
class Name(models.Model):
    name = models.CharField(max_length=20)

class Body(models.Model):
     description = models.TextField()

class About(models.Model):
      description = models.TextField()

class GalleryMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    media_type = models.CharField(max_length=5, choices=MEDIA_TYPE_CHOICES)
    image = models.ImageField(upload_to='gallery_images/', blank=True, null=True)
    video = models.FileField(upload_to='gallery_videos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


def __str__(self):
        return self.name