from django.shortcuts import render

# Create your views here.
def initial(request):
    return render(request,"app/index.html")