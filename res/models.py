from django.db import models


class Designation(models.Model):
    title = models.CharField(max_length=50, unique=True,
                             verbose_name="Специальность")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class Chef(models.Model):
    image = models.ImageField(upload_to='photos/chef',
                              verbose_name="Фото")
    full_name = models.CharField(max_length=50,
                                 verbose_name="Фамилия, имя")
    insta = models.CharField(max_length=50,
                             verbose_name="Инстаграм",
                             null=True, blank=True)
    twit = models.CharField(max_length=50,
                            verbose_name="Твиттер",
                            null=True, blank=True)
    face = models.CharField(max_length=50,
                            verbose_name="Фейсбук",
                            null=True, blank=True)
    designation = models.ForeignKey(to=Designation, on_delete=models.CASCADE,
                                    verbose_name="Специальность")

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Повар"
        verbose_name_plural = "Повара"


class Service(models.Model):
    icon = models.CharField(max_length=255,
                            verbose_name='Иконка сервиса')
    title = models.CharField(max_length=255,
                             verbose_name='Название сервиса')
    description = models.TextField(verbose_name='Описание сервиса')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'


class AboutImage(models.Model):
    image_1 = models.ImageField(upload_to='photos/about',
                                verbose_name="Фото 1")
    image_2 = models.ImageField(upload_to='photos/about',
                                verbose_name="Фото 2")
    image_3 = models.ImageField(upload_to='photos/about',
                                verbose_name="Фото 3")
    image_4 = models.ImageField(upload_to='photos/about',
                                verbose_name="Фото 4")

    def __str__(self):
        return "Фотография"

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Category(models.Model):
    icon = models.CharField(max_length=255,
                            verbose_name='Иконка сервиса')
    title = models.CharField(max_length=255,
                             verbose_name='Название категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Food(models.Model):
    image = models.ImageField(upload_to='photos/food',
                              verbose_name='Изображение')
    title = models.CharField(max_length=255,
                             verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'


class Reservation(models.Model):
    name = models.CharField(max_length=255,
                            verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    reservation_date = models.DateTimeField(verbose_name='Дата брони')
    people = models.IntegerField(verbose_name='Число людей')
    request = models.TextField(verbose_name='Спец. запрос')

    def __str__(self):
        return f"""{self.name} {self.reservation_date}"""

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'


class Testimonial(models.Model):
    feedback = models.CharField(max_length=255,
                                verbose_name='Отзыв')
    name = models.CharField(max_length=255,
                            verbose_name='Имя')
    profession = models.CharField(max_length=255,
                                  verbose_name='Профессия')
    photo = models.ImageField(upload_to='photos/client')

    def __str__(self):
        return f"""{self.name} {self.profession}"""

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
