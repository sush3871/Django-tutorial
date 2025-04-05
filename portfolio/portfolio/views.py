from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello, world. You're at the portfolio index.")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You're at the portfolio about.")

def contact(request):
    return HttpResponse("Hello, world. You're at the portfolio contact.")