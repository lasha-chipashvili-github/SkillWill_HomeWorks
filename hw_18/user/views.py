from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse
from .models import User
import datetime

def show_user(request):
    username = "Didier"
    userlastname = "Drogba"
    date_of_birth = "1978-03-11"

    start = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d")
    end = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
    print("this is start:", start)
    print("this is end:", end)

    age = (end.year - start.year)

    user = User.objects.all()
    print("this is prindet:", user)
    return HttpResponse(
        f"""
        <h1> username: {username} </h1>
        <h1> lastname: {userlastname} </1>
        <h1> age: {age} </h1>
        """
    )


