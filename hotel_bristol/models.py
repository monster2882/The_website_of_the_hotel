from django.db import models


class RoomReservation(models.Model):
    ROOM_TYPES = (
        ('standard', 'Обычный номер'),
        ('comfort', 'Комфортный номер'),
        ('luxury', 'Люкс номер'),
    )

    entry_date = models.DateField(verbose_name='Дата въезда')
    exit_date = models.DateField(verbose_name='Дата выезда')
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    number_of_people = models.PositiveIntegerField(verbose_name='Количество людей')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    room_type = models.CharField(max_length=10, choices=ROOM_TYPES, verbose_name='Тип номера')

    def __str__(self):
        return f'{self.full_name} - {self.room_type} - {self.entry_date} to {self.exit_date}'