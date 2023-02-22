from django.shortcuts import render
import datetime

# Create your views here.


def newyear(request):
    today = datetime.datetime.now()
    return render(
        request, "newyear/index.html", {"isnewyear": today.month == 1 and today.day == 1}
    )
