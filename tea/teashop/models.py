from django.db import models


class Category(models.Model):
    name = models.CharField('Катгория', max_length=200)
    description = models.TextField('Описание категории')
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField('Брэнд', max_length=40)
    description = models.TextField('Описание брэнда')
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField('Брэнд', max_length=40)
    description = models.TextField('Описание брэнда')
    url = models.SlugField(max_length=160, unique=True, null=True)

    def __str__(self):
        return self.name

class Tags(models.Model):
    name = models.CharField('Тэг', max_length=40)
    url = models.SlugField(max_length=160, unique=True,null=True)

    def __str__(self):
        return self.name


class Teapack(models.Model):
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание', null=True)
    cost = models.PositiveSmallIntegerField('Стоимость товара', default=0)
    odlcost = models.PositiveSmallIntegerField('Старая цена', default=None, blank=True, null=True)
    sale = models.PositiveSmallIntegerField('Скидка', default=None, null=True)
    url = models.SlugField(max_length=160, unique=True, blank=True, null=True)
    image = models.ImageField('Миниатюра товара', upload_to='media/', null=True)
    draft = models.BooleanField("Черновик", default=False)
    likestate = models.BooleanField('Лайк', default=False)
    brand = models.ManyToManyField(Brand)
    color = models.ManyToManyField(Color)
    tags = models.ManyToManyField(Tags, blank=True, related_name='tea')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        pass


class RaitingStar(models.Model):
    value = models.PositiveSmallIntegerField('Значение', default=0)

    def __str__(self):
        return self.value

class Raiting(models.Model):
    ip = models.CharField('IP адресс', max_length=15)
    star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE)
    tea = models.ForeignKey(Teapack, on_delete=models.CharField)

    def __str__(self):
        return self.ip

class Picture(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.TextField('Описание')
    image = models.ImageField('Изображение', upload_to='picture/')

    def __str__(self):
        return self.title

class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField('Имя', max_length=100)
    message = models.TextField('Сообщение', max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    tea = models.ForeignKey(Teapack, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.tea}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
