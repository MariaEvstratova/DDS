from django.http import HttpResponse
from django.shortcuts import render, redirect
from dds.models import MoneyOperation
from dds.forms import MoneyOperationForm, StatusForm, OperationTypeForm, CategoryForm, SubCategoryForm
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


def dicts(request):
    status = Status.objects.all()
    operation_type = OperationType.objects.all()
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    return render(request, "dicts.html", {"statuses": status,
                                          "operation_type": operation_type,
                                          "categories": category,
                                          "subcategories": subcategory})

def delete_status(request, id):
    status = Status.objects.get(id=id)
    status.delete()
    return redirect('/dicts')


def delete_operation_type(request, id):
    operation_type = OperationType.objects.get(id=id)
    operation_type.delete()
    return redirect('/dicts')


def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect('/dicts')


def delete_subcategory(request, id):
    subcategory = SubCategory.objects.get(id=id)
    subcategory.delete()
    return redirect('/dicts')


# Добавление статуса
def add_status(request):
    if request.method == "POST":
        # Добавление новой записи в бд при нажатии submit
        status = request.POST.get("status")
        operation = Status(name=status)
        operation.save()
        return redirect('/dict')
    else:
        # Отображение формы StatusForm
        statusform = StatusForm()
        return render(request, "rec.html", {"title": 'Создание cтатуса', "form": statusform})


# Изменение записи
def edit_status(request, id):
    if request.method == "POST":
        # Перезапись данных с новыми значениями, которые ввел пользователь
        status = Status.objects.get(id=id)
        status.name = request.POST.get("status")
        status.save()
        return redirect('/dicts')
    else:
        # Отображение формы с данными конкретной операции этого id
        status = Status.objects.get(id=id)
        statusform = StatusForm(instance=status)
        return render(request, "rec.html", {"title": 'Изменение статуса', "form": statusform})


# Добавление типа операции
def add_operation_type(request):
    if request.method == "POST":
        # Добавление новой записи в бд при нажатии submit
        operation_type = request.POST.get("operation_type")
        operation_type = OperationType(name=operation_type)
        operation_type.save()
        return redirect('/dicts')
    else:
        # Отображение формы OperationType
        operation_type_form = OperationTypeForm()
        return render(request, "rec.html", {"title": 'Создание типа операции', "form": operation_type_form})


# Изменение типа операции
def edit_operation_type(request, id):
    if request.method == "POST":
        # Перезапись данных с новыми значениями, которые ввел пользователь
        operation_type = OperationType.objects.get(id=id)
        operation_type.name = request.POST.get("operation_type")
        operation_type.save()
        return redirect('/dicts')
    else:
        # Отображение формы с данными конкретной операции этого id
        operation_type = OperationType.objects.get(id=id)
        operation_typeform = OperationTypeForm(instance=operation_type)
        return render(request, "rec.html", {"title": 'Изменение типа операции', "form": operation_typeform})


# Добавление категории
def add_category(request):
    if request.method == "POST":
        # Добавление новой записи в бд при нажатии submit
        category = request.POST.get("category")
        operation_type = OperationType.objects.get(id=int(request.POST.get("operation_type")))
        category = Category(name=category, operation_type=operation_type)
        category.save()
        return redirect('/dicts')
    else:
        # Отображение формы OperationType
        categoryform = CategoryForm()
        return render(request, "rec.html", {"title": 'Создание категории', "form": categoryform})


# Изменение категории
def edit_category(request, id):
    if request.method == "POST":
        # Перезапись данных с новыми значениями, которые ввел пользователь
        category = Category.objects.get(id=id)
        category.name = request.POST.get("category")
        category.operation_type = OperationType.objects.get(id=int(request.POST.get("operation_type")))
        category.save()
        return redirect('/dicts')
    else:
        # Отображение формы с данными конкретной операции этого id
        category = Category.objects.get(id=id)
        categoryform = CategoryForm(instance=category)
        return render(request, "rec.html", {"title": 'Изменение категории', "form": categoryform})


# Добавление подкатегории
def add_subcategory(request):
    if request.method == "POST":
        # Добавление новой записи в бд при нажатии submit
        subcategory = request.POST.get("subcategory")
        category = Category.objects.get(id=int(request.POST.get("category")))
        subcategory = SubCategory(name=subcategory, category=category)
        subcategory.save()
        return redirect('/dicts')
    else:
        # Отображение формы OperationType
        subcategoryform = SubCategoryForm()
        return render(request, "rec.html", {"title": 'Создание подкатегории', "form": subcategoryform})


# Изменение подкатегории
def edit_subcategory(request, id):
    if request.method == "POST":
        # Перезапись данных с новыми значениями, которые ввел пользователь
        subcategory = SubCategory.objects.get(id=id)
        subcategory.name = request.POST.get("subcategory")
        subcategory.category = Category.objects.get(id=int(request.POST.get("category")))
        subcategory.save()
        return redirect('/dicts')
    else:
        # Отображение формы с данными конкретной операции этого id
        category = SubCategory.objects.get(id=id)
        categoryform = SubCategoryForm(instance=category)
        return render(request, "rec.html", {"title": 'Изменение подкатегории', "form": categoryform})