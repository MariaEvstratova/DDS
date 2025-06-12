from django.shortcuts import render
# from .forms import UserForm
from dds.models import MoneyOperation


def index(request):
    moneyoperations = MoneyOperation.objects.all()
    return render(request, "index.html", {"operations": moneyoperations})


def add_operation(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        return HttpResponse(f"<h2>Привет, {name}, твой возраст: {age}</h2>")
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform})
    return render(request, "rec.html", {"operations": moneyoperations})


def delete_operation(request):
    moneyoperations = MoneyOperation.objects.all()
    return render(request, "rec.html", {"operations": moneyoperations})

