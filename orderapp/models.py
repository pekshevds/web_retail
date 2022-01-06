from django.db import models
from django.db.models import Sum


from customerapp.models import Customer
from catalogapp.models import Product


import uuid
# Create your models here.

class Order(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    order_date = models.DateTimeField(verbose_name='Дата заказа', auto_now_add=True)
    order_number = models.IntegerField(verbose_name='Номер заказа', null=True, blank=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='Заказчик')
    total = models.DecimalField(verbose_name='Всего', max_digits=15, decimal_places=2, default=0)

    @property
    def representation(self):
        return f'{self.order_number} от {self.order_date}'

    def __str__(self):
        return self.representation

    def save(self, *args, **kwargs):

        self.total = self.items.aggregate(total=Sum('total'))['total']

        if self.order_number == 0:
            self.order_number = Order.objects.all().count() + 1
        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ покупателя'
        verbose_name_plural = 'Заказы покупателей'
        ordering = ['-order_date']

class ItemOrder(models.Model):
    
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items', null=True)
    
    product = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Номенклатура', null=True, blank=True)
    price = models.DecimalField(verbose_name='Цена', max_digits=15, decimal_places=2, default=0)
    quant = models.DecimalField(verbose_name='Количество', max_digits=15, decimal_places=3, default=0)    
    total = models.DecimalField(verbose_name='Всего', max_digits=15, decimal_places=2, default=0)


    item_number = models.IntegerField(verbose_name='Номер строки', null=True, blank=True)

    def __str__(self):
        return f'{self.item_number}'

    def save(self, *args, **kwargs):

        if self.item_number == 0:
            self.item_number = ItemOrder.objects.filter(order=self.order).count() + 1
        super(ItemOrder, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Строка заказа покупателя'
        verbose_name_plural = 'Строки заказа покупателя'
        ordering = ['item_number']