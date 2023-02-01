from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def main(request):
    return HttpResponse("<h1>This is my first django app page!! Hello everyone</h1>")