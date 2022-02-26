from django.db import models


class Order(models.Model):
    PHONE = 'phone'
    TV = 'tv'
    COMPUTER = 'computer'
    TYPE = [
        (PHONE, 'Телефон'),
        (TV, 'Телевизор'),
        (COMPUTER, 'Компьютер'),
    ]

    product = models.CharField('Название товара', max_length=50)
    type = models.CharField('Тип', max_length=50, choices=TYPE)
    delivery_date = models.DateField('Дата доставки')
    file = models.FileField('Файл', upload_to='orders/', blank=True, null=True)

    class Meta:
        ordering = ['delivery_date']

    def __str__(self):
        return f'{self.product} ({self.delivery_date})'


class Address(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='addresses',
        verbose_name='Заказ'
    )
    address = models.CharField('Адрес пункта выдачи', max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.address
