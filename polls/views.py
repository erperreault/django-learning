from django.shortcuts import HttpResponse

def index(request):
    # always return HttpResponse or an Exception
    return HttpResponse("Hello, world. You're at the polls index.")
