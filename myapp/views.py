from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def pcOne(request):
    return render(request,'pc_one.html')