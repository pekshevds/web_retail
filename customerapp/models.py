from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Customer(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, verbose_name='Пользователь', related_name='customer', on_delete=models.PROTECT)
    name = models.CharField(verbose_name='Наименование', max_length=100, blank=False, null=False, default='')
    code = models.CharField(verbose_name='Код', max_length=11, blank=True, null=True, default='')
    inn = models.CharField(verbose_name='ИНН', max_length=12, blank=True, null=True, default='')
    kpp = models.CharField(verbose_name='КПП', max_length=9, blank=True, null=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'        
