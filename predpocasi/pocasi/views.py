from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Place
from .forms import PlaceForm


def index(request):
    places = Place.objects.filter(user=request.user)
    return render(request, "index.html", {"places": places})

@login_required
def add_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.add_message(request, messages.INFO, "Trať je přidána")
            return redirect("index")
    else:
        form = PlaceForm()
    return render(request, "add_place.html",  {"form": form})
