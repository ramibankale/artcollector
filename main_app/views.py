from django.shortcuts import render

# Add this arts list below the imports
arts = [
  {'name': 'Lolo', 'breed': 'tabby', 'description': 'furry little demon', 'age': 3},
  {'name': 'Sachi', 'breed': 'calico', 'description': 'gentle and loving', 'age': 2},
]

# Create your views here.
# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def arts_index(request):
  # We pass data to a template very much like we did in Express!
  return render(request, 'arts/index.html', {
    'arts': arts
  })