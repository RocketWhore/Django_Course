from django.db import models
from django.utils import timezone

NULLABLE = {'blank':  True, 'null': True}

class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    slug = models.CharField(max_length=150, verbose_name='slug')
    body = models.TextField()
    preview = models.ImageField(upload_to='materials_image', **NULLABLE)
    date_of_create = models.DateTimeField(default=timezone.now, **NULLABLE)
    sign_of_pub = models.BooleanField(default=False, **NULLABLE)
    count_view = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'материал'
        verbose_name_plural = 'материалы'
