from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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
  arts = Art.objects.all() # Retrieve all arts
  # We pass data to a template very much like we did in Express!
  return render(request, 'arts/index.html', {
    'arts': arts
  })
def arts_detail(request, art_id):
  art = Art.objects.get(id=art_id)
  return render(request, 'arts/detail.html', { 'art': art })

class ArtCreate(CreateView):
  model = Art
  fields = '__all__'

class ArtUpdate(UpdateView):
  model = Art
  # Let's disallow the renaming of a art by excluding the name field!
  fields = ['culture', 'description', 'age', 'origin']

class ArtDelete(DeleteView):
  model = Art
  success_url = '/arts'
