from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'recipes/home.html')
def index(request):
    return render(request,   'recipes/index.html')