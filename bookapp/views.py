from django.shortcuts import HttpResponse

def home_page_view(request):
    return HttpResponse("Hello, word!")

from django.views.generic import TemplateView

#templates
class HomePageView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):  
    template_name = "about.html"



    template_name = "about.html"
# Create your views here.
