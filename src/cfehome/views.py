import pathlib
from django.http import HttpResponse
from django.shortcuts import render 

from visits.models import PageVisit


this_dir = pathlib.Path(__file__).resolve().parent

def about_page_view(request, *args, **kwargs):
    PageVisit.objects.create(path=request.path)
    total_count = PageVisit.objects.all().count()
    queryset = PageVisit.objects.filter(path=request.path)
    
    # Handle zero division error 
    try:
        percent = (queryset.count() * 100.0) / total_count 
    except:
        percent = 0 
    
    my_title = "My Page" 
    my_context = {
        "page_title": my_title,
        "percent": f"{percent:.2f}", 
        "page_visit_count": queryset.count(),
        "total_count": total_count
    }
    html_template = "home.html"
    return render(request, html_template, my_context)

def home_page_view(request, *args, **kwargs):
    PageVisit.objects.create(path=request.path)
    total_count = PageVisit.objects.all().count()
    queryset = PageVisit.objects.filter(path=request.path)
    
    # Handle zero division error 
    try:
        percent = (queryset.count() * 100.0) / total_count 
    except:
        percent = 0 
    
    my_title = "My Page" 
    my_context = {
        "page_title": my_title,
        "percent": f"{percent:.2f}", 
        "page_visit_count": queryset.count(),
        "total_count": total_count
    }
    html_template = "home.html"
    return render(request, html_template, my_context)

def my_old_home_page_view(request, *args, **kwargs):
    my_title = "My Page" 
    my_context = {
        "page_title": my_title, 
    }
    html_ = """
    <!Doctype html>
    <html>
    <body>
    <h1>{page_title} anything?</h1>
    </body>
    </html>
    """.format(**my_context)
    return HttpResponse(html_)