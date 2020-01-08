from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "web_blog/home.html")


# views always need to return a httpresponse or an exception, so when we use


def about(request):
    return render(request, "web_blog/about.html")

