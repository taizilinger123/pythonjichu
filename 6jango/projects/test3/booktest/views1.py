from django.http import HttpResponse

def index(request):
    return HttpResponse('hello 123')

#http://127.0.0.1:8000/booktest/