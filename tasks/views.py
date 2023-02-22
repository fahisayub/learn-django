from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


class NewForm(forms.Form):
    task = forms.CharField(label="Newtask")


def tasks(request):
    if "task" not in request.session:
        request.session["task"] = []

    return render(request, "tasks/index.html", {"tasks": request.session["task"]})


def addtask(request):
    if request.method == "POST":
        form = NewForm(request.POST)
        if form.is_valid():
            taskdata = form.cleaned_data["task"]
            request.session["task"] += [taskdata]
            return HttpResponseRedirect(reverse("tasks:tasks"))
        else:
            return render(request, "tasks/addtask.html", {"form": form})
    return render(request, "tasks/addtask.html", {"form": NewForm()})
