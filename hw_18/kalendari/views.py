from django.shortcuts import render
from django.http import HttpResponse
from datetime import date
from .models import Kalendari

# Create your views here.
def tarigi(request):
    today = date.today()
    this_day = Kalendari.objects.values()
    print("this is printed:", this_day)
    return HttpResponse(
        f"""
        <h1> დღეს არის: {today}
        """
    )