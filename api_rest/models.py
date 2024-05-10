from django.db import models

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=150, default='')
    product_amount = models.IntegerField(default='')
    product_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'id: {self.product_id} | Produto: {self.product_name}'
    