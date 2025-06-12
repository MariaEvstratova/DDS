from django.db import models


class Status(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class OperationType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    operation_type = models.ForeignKey(OperationType, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'operation_type')

    def __str__(self):
        return f"{self.name} ({self.operation_type})"


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name', 'category')

    def __str__(self):
        return f"{self.name} ({self.category})"


class MoneyOperation(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    operation_date = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    operation_type = models.ForeignKey(OperationType, on_delete=models.PROTECT)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.operation_date} - {self.amount} ({self.status})"
