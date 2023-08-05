from django.shortcuts import HttpResponse

def home_page_view(request):
    return HttpResponse("Hello, word!")

# Create your views here.
