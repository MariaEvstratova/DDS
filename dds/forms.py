from django import forms
from .models import MoneyOperation, Status, OperationType, Category, SubCategory


# Форма добавления операции ддс
class MoneyOperationForm(forms.Form):
    operation_date = forms.DateField(
        label='Дата операции',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        label='Статус'
    )

    operation_type = forms.ModelChoiceField(
        queryset=OperationType.objects.all(),
        label='Тип операции'
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория'
    )

    subcategory = forms.ModelChoiceField(
        queryset=SubCategory.objects.all(),
        label='Подкатегория'
    )

    amount = forms.DecimalField(
        label='Сумма',
        max_digits=12,
        decimal_places=2
    )

    comment = forms.CharField(
        label='Комментарий',
        widget=forms.Textarea,
        required=False
    )


    # Обновление данных из instance
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields['operation_date'].initial = instance.operation_date
            self.fields['status'].initial = instance.status
            self.fields['operation_type'].initial = instance.operation_type
            self.fields['category'].initial = instance.category
            self.fields['subcategory'].initial = instance.subcategory
            self.fields['amount'].initial = instance.amount
            self.fields['comment'].initial = instance.comment


# Форма добавления статуса
class StatusForm(forms.Form):
    status = forms.CharField(
        label='Статус'
    )


# Форма добавления типа операции
class OperationTypeForm(forms.Form):
    operation_type = forms.CharField(
        label='Тип операции'
    )


# Форма добавления категории
class CategoryForm(forms.Form):
    category = forms.CharField(
        label='Категория'
    )

    operation_type = forms.ModelChoiceField(
        queryset=OperationType.objects.all(),
        label='Тип операции'
    )

    # Обновление данных из instance
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields['category'].initial = instance.category
            self.fields['operation_type'].initial = instance.operation_type


# Форма добавления подкатегории
class SubCategoryForm(forms.Form):
    subcategory = forms.CharField(
        label='Подкатегория'
    )

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        label='Категория'
    )

    # Обновление данных из instance
    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance', None)
        super().__init__(*args, **kwargs)

        if instance:
            self.fields['subcategory'].initial = instance.subcategory
            self.fields['category'].initial = instance.category

