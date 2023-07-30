from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Art
from .forms import DisplayForm

# Add this arts list below the imports

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
  display_form = DisplayForm()
  return render(request, 'arts/detail.html', { 'art': art, 'display_form': display_form})

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

def add_display(request, art_id):
  # create a ModelForm instance using the data in request.POST
  form = DisplayForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the art_id assigned
    new_display = form.save(commit=False)
    new_display.art_id = art_id
    new_display.save()
  return redirect('detail', art_id=art_id)
