from django.db import models


class Task (models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title


# в командной строке
# Далее переходим в терминал python3 manage.py makemigrations - создали миграции
# Выполним меграции python3 manage.py migrate

# сюда не относиться
# python3 manage.py createsuperuser - создание пользователя

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
