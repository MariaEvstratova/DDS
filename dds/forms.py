from django import forms
from dds.models import Status
from dds.models import OperationType
from dds.models import Category
from dds.models import SubCategory

# class Status(forms.Form):
#     name = forms.CharField(max_length=100)
#
#
#
# class OperationType(forms.Form):
#     name = forms.CharField(max_length=100)
#
#
# class Category(forms.Form):
#     name = forms.CharField(max_length=100)
#     operation_type = forms.ForeignKey(OperationType, on_delete=models.CASCADE)
#
#
# class SubCategory(forms.Form):
#     name = forms.CharField(max_length=100)
#     category = forms.ForeignKey(Category, on_delete=models.CASCADE)


class MoneyOperationForm(forms.Form):
    operation_date = forms.DateField()
    status_choices = [(status.id, status.name) for status in Status.objects.all()]

    status = forms.ChoiceField(
        choices=status_choices,
        label="Статус операции",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    operation_type_choices = [(type.id, type.name) for type in OperationType.objects.all()]

    operation_type = forms.ChoiceField(
        choices=operation_type_choices,
        label="Тип операции",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    category_choices = [(category.id, category.name) for category in Category.objects.all()]

    category = forms.ChoiceField(
        choices=category_choices,
        label="Категория",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    subcategory_choices = [(subcategory.id, subcategory.name) for subcategory in SubCategory.objects.all()]

    subcategory = forms.ChoiceField(
        choices=subcategory_choices,
        label="Подкатегория",
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    comment = forms.CharField(widget=forms.Textarea, required=False)
