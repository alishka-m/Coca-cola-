from django.db import models

class Films(models.Model):
    GENRE_CHOICE = (
        ('Ужасы, ужасы')
        ('Комедия, Комедия')
        ('Боевик, Боевик')
    )
    image = models.ImageField(upload_to='films/', verbose_name='Загрузите картинку:')
    title = models.CharField(max_length=100, verbose='Укажите название')
    price = models.FloatField(verbose_name='Укажите цену')
    date_start_film = models.DateField(verbose_name='Введите дату выхода')
    genre = models.CharField(max_length=100, choices=GENRE_CHOICE, default='Комедия',
                             verbose_name='Укажите жанр')

