from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    first_page = """<!DOCTYPE html>
      <html lang="en">
      <head>
          <meta charset="UTF-8">
          <title>Title</title>
      </head>
      <body>
      <h1>МОЯ ПЕРВАЯ СТРАНИЦА</h1>
      <p><a href="about">About me</a></p>
      </body>
      </html>"""
    return HttpResponse(first_page)


def about(request):
    return HttpResponse("About us")





