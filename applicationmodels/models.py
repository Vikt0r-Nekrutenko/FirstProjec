from django.db import models

# Create your models here.

class Example(models.Model):
    int_field                    = models.IntegerField
    positive_int_field           = models.PositiveIntegerField
    positiver_small_int_field    = models.PositiveSmallIntegerField
    big_int_field                = models.BigIntegerField
    float_field                  = models.FloatField
    binary_field                 = models.BinaryField
    boolean_field                = models.BooleanField
    char_field                   = models.CharField(max_length=5)
    text_field                   = models.TextField(max_length=20)
    date_field                   = models.DateField(auto_now=False)
    date_time_field              = models.DateTimeField(auto_now_add=False)
    decimal_field                = models.DecimalField(max_digits=8, decimal_places=2)
    email_field                  = models.EmailField()
    file_field                   = models.FileField
    image_field                  = models.ImageField

class Author(models.Model):
    name     = models.TextField(max_length=50, verbose_name = "Iм'я")
    surname  = models.TextField(max_length=50, verbose_name = "Прiзвище")
    birthday = models.DateField(auto_now=False, verbose_name = "День народження")

    def __str__(self):
        return "Iм'я: %s, Прiзвище: %s" % (self.name, self.surname)

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"

class Book(models.Model):
    GENRE_LIST = (
        ('detective', 'Детектив'),
        ('thriller', 'Триллер'),
        ('drama', 'Драма'),
        ('roman', 'Роман'),
        ('comics', 'Комiкс'),
        ('prose', 'Проза'),
    )
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    name = models.TextField(max_length=50, verbose_name="Назва")
    description = models.TextField(max_length=1000, verbose_name="Опис")
    genre = models.CharField(max_length=50, choices=GENRE_LIST)

    def __str__(self):
        return "Назва: %s" % (self.name)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

class Place(models.Model):
    name = models.TextField(max_length=50, verbose_name="Назва")
    address = models.TextField(max_length=50, verbose_name="Адреса")

    def __str__(self):
        return "Назва: %s" % (self.name)

class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    home_delivery = models.BooleanField(False)
    noctidial = models.BooleanField(False)

    def __str__(self):
        return "Назва: %s" % (self.place.name)

class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.TextField(max_length=50, verbose_name="Iм'я")

    def __str__(self):
        return "Iм'я: %s, Назва ресторану: %s" % (self.name, self.restaurant.place.name)

class Publication(models.Model):
    name = models.TextField(max_length=50, verbose_name="Назва")

    def __str__(self):
        return "Назва: %s" % (self.name)

class Article(models.Model):
    name = models.TextField(max_length=50, verbose_name="Назва")
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return "Назва: %s" % (self.name)