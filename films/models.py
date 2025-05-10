from django.db import models

class Film(models.Model):
    title = models.CharField(max_length=255, verbose_name="Укажите название фильма")
    relase_date = models.DateTimeField(auto_now_add=True)
    genre = models.CharField(max_length=255 , verbose_name="Укажите жанр", default="фантастика")
    author = models.CharField(max_length=255, verbose_name="Укажите автора")
    description = models.TextField(verbose_name="Укажите описание фильма")
    trailer_url = models.URLField(verbose_name="Вставьте ссылку фильма",blank=True,null=True)
     
    def __str__(self):
       return self.title