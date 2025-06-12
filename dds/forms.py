from django import forms


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


# class MoneyOperation(forms.Form):
#     created_at = forms.DateTimeField(auto_now_add=True)
#     operation_date = forms.DateField()
#     status = forms.ForeignKey(Status, on_delete=models.PROTECT)
#     operation_type = forms.ForeignKey(OperationType, on_delete=models.PROTECT)
#     category = forms.ForeignKey(Category, on_delete=models.PROTECT)
#     subcategory = forms.ForeignKey(SubCategory, on_delete=models.PROTECT)
#     amount = forms.DecimalField(max_digits=12, decimal_places=2)
#     comment = forms.TextField(blank=True, null=True)
