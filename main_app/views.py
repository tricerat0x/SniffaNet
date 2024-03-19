from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def user(request):
  return render(request, 'user.html')

def reports(request):
  return render(request, 'reports/index.html')