from django.shortcuts import render


# Create your views here.
def pub_b2b(request):
    return render(request, 'home/index.html')
