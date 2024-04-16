from django.db import models
from django.contrib.auth import get_user_model


class Omonimlar(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'omonimlar'
        verbose_name = 'Omonimlar'
        ordering = ('name',)
