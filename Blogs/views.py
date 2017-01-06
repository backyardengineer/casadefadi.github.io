from django.shortcuts import render

def homepage(req):
    return render(req, "index.html")

def aboutMe(req):
    return render(req, "about-me.html")

def blog(req):
    return render(req, "blog.html")

def elements(req):
    return render(req, "elements.html")
