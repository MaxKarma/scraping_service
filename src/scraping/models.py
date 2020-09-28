from django.db import models
from .translit import transliterate as trl

# Create your models here.


class City(models.Model):
    name = models.CharField('Название населенного пункта', max_length=50, unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name='Название населенного пункта'
        verbose_name_plural='Название населенноых пунктов'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = trl(self.name).lower()
        super().save(*args, **kwargs)


class Language(models.Model):
    name = models.CharField('Язык прогрммирования', max_length=50, unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Язык прогрммирования'
        verbose_name_plural = 'Языки прогрммирования'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = trl(self.name).lower()
        super().save(*args, **kwargs)


class Vacancy(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField('Заголовок вакансии', max_length=250)
    company = models.CharField('Компания', max_length=250)
    description = models.TextField('Описание вакансии')
    city = models.ForeignKey('City',on_delete=models.CASCADE, verbose_name='Город')
    language = models.ForeignKey('Language',on_delete=models.CASCADE, verbose_name='Язык программировани я')
    timestamp = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

