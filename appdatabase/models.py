from django.db import models

# Create your models here.

class Human(models.Model):
    IT_COMPANY = (
        ('soft_serve', 'SoftServe'),
        ('daxx_bv', 'Daxx BV'),
        ('levi9_ukraine', 'Levi9 Ukraine'),
        ('evoplay', 'Evoplay'),
        ('apriorit', 'Apriorit'),
    )
    IT_POSITION = (
        ('developer', 'Developer'),
        ('devops', 'DevOps'),
        ('manager', 'Manager'),
    )
    IT_LANG = (
        ('ruby', 'Ruby'),
        ('python', 'Python'),
        ('java', 'Java'),
        ('asm', 'Assembler'),
        ('cpp', 'C++'),
    )
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birth = models.DateField(auto_now=False)
    company = models.CharField(max_length=150, choices=IT_COMPANY)
    position = models.CharField(max_length=15, choices=IT_POSITION)
    language = models.CharField(max_length=10, choices=IT_LANG, default=IT_LANG[0])

    def __str__(self):
        return "Фамилия: %s Имя: %s Компания: %s" % (self.name, self.surname, self.company)

    class Meta:
        verbose_name = "Человечек"
        verbose_name_plural = "Человечеки"