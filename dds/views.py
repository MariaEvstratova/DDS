from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import UserForm
from dds.models import MoneyOperation
from dds.forms import MoneyOperationForm
from dds.models import Status
from dds.models import OperationType
from dds.models import Category
from dds.models import SubCategory


def index(request):
    moneyoperations = MoneyOperation.objects.all()
    return render(request, "index.html", {"operations": moneyoperations})


def add_operation(request):
    if request.method == "POST":
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
        moneyoperationform = MoneyOperationForm()
        return render(request, "rec.html", {"title": 'Создание записи о движении денежных средств', "form": moneyoperationform})
    return redirect('/')


def edit_operation(request, id):
    if request.method == "POST":
        operation = Status.objects.get(id=id)
        operation.operation_date = request.POST.get("operation_date")
        operation.status = Status.objects.get(id=int(request.POST.get("status")))
        operation.operation_type = OperationType.objects.get(id=int(request.POST.get("operation_type")))
        operation.category = Category.objects.get(id=int(request.POST.get("category")))
        operation.subcategory = SubCategory.objects.get(id=int(request.POST.get("subcategory")))
        operation.amount = request.POST.get("amount")
        operation.comment = request.POST.get("comment")
        operation.save()
        # operation = MoneyOperation(operation_date=operation_date,
        #                            status=status,
        #                            operation_type=operation_type,
        #                            category=category,
        #                            subcategory=subcategory,
        #                            amount=amount,
        #                            comment=comment)
        return redirect('/')
    else:
        operation = MoneyOperation.objects.get(id=id)
        initial_data = {"operation_date": operation.operation_date,
                        "status": operation.status.name,
                        "operation_type": operation.operation_type.name,
                        "category": operation.category.name,
                        "subcategory": operation.subcategory.name,
                        "amount": operation.amount,
                        "comment": operation.comment}
        moneyoperationform = MoneyOperationForm(initial=initial_data)
        # moneyoperationform.operation_date.data = operation.operation_date
        # moneyoperationform.status.value = operation.status
        # moneyoperationform.operation_type.value = operation.operation_type
        # moneyoperationform.category.value = operation.category
        # moneyoperationform.subcategory.value = operation.subcategory
        # moneyoperationform.amount.value = operation.amount
        # moneyoperationform.comment.value = operation.comment
        return render(request, "rec.html", {"title": 'Изменение записи о движении денежных средств', "form": moneyoperationform})

#
# def delete_operation(request):
#     moneyoperations = MoneyOperation.objects.all()
#     return render(request, "rec.html", {"operations": moneyoperations})

