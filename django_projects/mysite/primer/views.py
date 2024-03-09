# mysite/primers/views.py

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the primer index.", content_type="text/plain")