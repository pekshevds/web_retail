import uuid

from django.db import models

#Соответствует 1С:Розница 2.2..11.29

class Brand(models.Model):
    """Марка (бренд)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Наименование', max_length=100, blank=False, null=False)
    code = models.CharField(verbose_name='Код', max_length=9, blank=True, null=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Торговая марка (Бренд)'
        verbose_name_plural = 'Торговые марки (Бренды)'

class Manufacturer(models.Model):
    """Производитель"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Наименование', max_length=100, blank=False, null=False)
    code = models.CharField(verbose_name='Код', max_length=9, blank=True, null=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Country(models.Model):
    """Страна ОКСМ"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Наименование', max_length=60, blank=False, null=False)
    code = models.CharField(verbose_name='Код', max_length=3, blank=True, null=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны мира (по ОКСМ)'

class Unit(models.Model):
    """Единица измерения ОКЕИ"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Наименование', max_length=25, blank=False, null=False)
    code = models.CharField(verbose_name='Код', max_length=4, blank=True, null=True, default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы (по ОКЕИ)'

class Category(models.Model):
    """Категория (Вид номенклатуры)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Наименование', max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория (вид номенклатуры)'
        verbose_name_plural = 'Категории (виды номенклатуры)'

class Product(models.Model):
    """Продукт-товар (Номенклатура с типом Товар)"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Наименование', max_length=100, blank=False, null=False)
    code = models.CharField(verbose_name='Код', max_length=11, blank=True, null=True, default='')
    art = models.CharField(verbose_name='Артикул', max_length=25, blank=True, null=True, default='')

    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, verbose_name='Марка (бренд)', blank=True, null=True)
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT, verbose_name='Производитель', blank=True, null=True)
    country = models.ForeignKey('Country', on_delete=models.PROTECT, verbose_name='Страна происхождения', blank=True, null=True)
    unit = models.ForeignKey('Unit', on_delete=models.PROTECT, verbose_name='Единица измерения', blank=False, null=False)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Вид номенклатуры', blank=False, null=False)

    descriptions = models.TextField(verbose_name='Описание', blank=True, null=True, default='')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'