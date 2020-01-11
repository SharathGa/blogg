from django.shortcuts import render
from django.http import HttpResponse

posts = [
    # this dummy data is a list of dictionaries.
    {
        "author": "Sharath Gangalapadu",
        "title": "First Blog post",
        "content": "First Post Content",
        "date-posted": "January 10, 2020",
    },
    {
        "author": "Angelina",
        "title": "Second Blog post",
        "content": "Bhai this no fap is difficult to control ",
        "date-posted": "January 10, 2020",
    },
]
# Create your views here.
def home(request):
    context = {"posts": posts}
    return render(request, "web_blog/home.html", context,)


# views always need to return a httpresponse or an exception, so when we use


def about(request):
    return render(request, "web_blog/about.html", {"title": " About"})

