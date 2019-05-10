from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request, 'home/home.html')

def home(request):
    return render(request, 'home/home.html')
def aboutme(request):
    return render(request, 'aboutme.html')
def ob(request):
    return render(request, 'home/ob.html')
def ee(request):
    return render(request, 'home/e&e.html')
def sc(request):
    return render(request, 'home/s&c.html')