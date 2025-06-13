from django.http import HttpResponse
from django.shortcuts import render, redirect
from dds.models import MoneyOperation
from dds.forms import MoneyOperationForm
from dds.models import Status
from dds.models import OperationType
from dds.models import Category
from dds.models import SubCategory


# Начальная страница с отображением записей
def index(request):
    moneyoperations = MoneyOperation.objects.all()
    return render(request, "index.html", {"operations": moneyoperations})


# Добавление записи
def add_operation(request):
    if request.method == "POST":
        # Добавление новой записи в бд при нажатии submit
        operation_date = request.POST.get("operation_date")
        status = Status.objects.get(id=int(request.POST.get("status")))
        operation_type = OperationType.objects.get(id=int(request.POST.get("operation_type")))
        category = Category.objects.get(id=int(request.POST.get("category")))
        subcategory = SubCategory.objects.get(id=int(request.POST.get("subcategory")))
        amount = int(request.POST.get("amount"))
        comment = request.POST.get("comment")
        operation = MoneyOperation(operation_date=operation_date,
                                   status=status,
                                   operation_type=operation_type,
                                   category=category,
                                   subcategory=subcategory,
                                   amount=amount,
                                   comment=comment)
        operation.save()
        return redirect('/')
    else:
        # Отображение формы MoneyOperationForm
        moneyoperationform = MoneyOperationForm()
        return render(request, "rec.html", {"title": 'Создание записи о движении денежных средств', "form": moneyoperationform})
    return redirect('/')


# Изменение записи
def edit_operation(request, id):
    if request.method == "POST":
        # Перезапись данных с новыми значениями, которые ввел пользователь
        operation = MoneyOperation.objects.get(id=id)
        operation.operation_date = request.POST.get("operation_date")
        operation.status = Status.objects.get(id=int(request.POST.get("status")))
        operation.operation_type = OperationType.objects.get(id=int(request.POST.get("operation_type")))
        operation.category = Category.objects.get(id=int(request.POST.get("category")))
        operation.subcategory = SubCategory.objects.get(id=int(request.POST.get("subcategory")))
        operation.amount = request.POST.get("amount")
        operation.comment = request.POST.get("comment")
        operation.save()
        return redirect('/')
    else:
        # Отображение формы с данными конкретной операции этого id
        operation = MoneyOperation.objects.get(id=id)
        moneyoperationform = MoneyOperationForm(instance=operation)
        return render(request, "rec.html", {"title": 'Изменение записи о движении денежных средств', "form": moneyoperationform})


# Удаление записи
def delete_operation(request, id):
    operation = MoneyOperation.objects.get(id=id)
    operation.delete()
    return redirect('/')
