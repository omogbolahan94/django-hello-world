from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


# here is a function-based view
def homePageView(request):
    return HttpResponse('Hello, World!')


# here is a class-based view
class HomePageView(TemplateView):
    """
    TemplateView already contains all the logic needed to display
    our template, we just need to specify the template’s name
    """
    template_name = 'home.html'