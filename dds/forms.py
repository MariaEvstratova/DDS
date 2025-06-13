from django import forms
from .models import MoneyOperation, Status, OperationType, Category, SubCategory


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
            # Динамически заполняем queryset для зависимых полей
        #     if instance.operation_type:
        #         self.fields['category'].queryset = Category.objects.filter(
        #             operation_type=instance.operation_type
        #         )
        #     if instance.category:
        #         self.fields['subcategory'].queryset = SubCategory.objects.filter(
        #             category=instance.category
        #         )
        #
        # # Добавляем обработчики изменений для динамического обновления полей
        # self.fields['operation_type'].widget.attrs.update({
        #     'onchange': 'updateCategories()'
        # })
        # self.fields['category'].widget.attrs.update({
        #     'onchange': 'updateSubcategories()'
        # })