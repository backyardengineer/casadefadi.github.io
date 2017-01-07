from django.shortcuts import render
from .models import BlogsModel


def homepage(req):
    return render(req, "index.html")

def aboutMe(req):
    return render(req, "about-me.html")

def blog(req):
    blogs = BlogsModel.objects.filter(discoverable=True)
    return render(req, "blog.html", {"blogs" : blogs})

def elements(req):
    return render(req, "elements.html")
