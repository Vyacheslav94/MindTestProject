from django.db import models

# class Registration(models.Model):
#     username = '',
#     password = ''
class Artiles(models.Model):
    title = models.CharField('Название', max_length=50)
    variants = models.CharField('Вариант ответа', max_length=50)
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата создания')

    def __str__(self):
        return self.title