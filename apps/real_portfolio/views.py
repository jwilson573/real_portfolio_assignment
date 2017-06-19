from django.shortcuts import render

def index(request):
    return render(request, "real_portfolio/index.html")

def projects(request):
    return render(request, "real_portfolio/projects.html")

def about(request):
    return render(request, "real_portfolio/about.html")

def testimonials(request):
    return render(request, "real_portfolio/testimonials.html")
