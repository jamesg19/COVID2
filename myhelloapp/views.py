from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
import pathlib
import os
import csv
from os import remove
# Create your views here.


def home(request):
    
    return render(request,'principal.html')
