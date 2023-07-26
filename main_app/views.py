from django.shortcuts import render
from .models import Art


# Add this arts list below the imports


# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def arts_index(request):
  arts = Art.objects.all() # Retrieve all cats
  # We pass data to a template very much like we did in Express!
  return render(request, 'arts/index.html', {
    'arts': arts
  })