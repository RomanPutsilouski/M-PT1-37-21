import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Art(models.Model):
    art_title = models.CharField('Заголовок', max_length=50)
    art_text = models.TextField('Статья')
    art_date_pub = models.DateTimeField('Дата публиации статьи')

    def __str__(self):
        return self.art_title

    def was_published_recently(self):
        return self.art_date_pub >= (timezone.now() - datetime.timedelta(days=7))

    class Meta:
        verbose_name = "Cтатья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    art = models.ForeignKey(Art, on_delete=models.CASCADE)
    сom_autor = models.CharField('Автор комментария', max_length=30)
    com_text = models.CharField('Текст комментария', max_length=100)

    def __str__(self):
        return self.сom_autor

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"