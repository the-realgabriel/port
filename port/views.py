from django.shortcuts import render
from .models import Name, Body, About, GalleryMedia
# Create your views here.

def home(request):
    names = Name.objects.all()  # Fetch names from the database
    bodies = Body.objects.all()
    about = About.objects.all()
    return render(request, 'index.html', {'names': names, 'bodies': bodies, 'about':about}) 

def contact(request):
    return render(request, 'contact.html')

def gallary(request):
      media_items = GalleryMedia.objects.all()
      return render(request, 'gallary.html', {'media_items': media_items})


