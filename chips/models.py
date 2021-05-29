from django.db import models


class Chip(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    company = models.CharField(max_length=100)

    # chip 이 가지고 있는 meta를 가져옴
    class Meta:
        verbose_name_plural = "스낵 관리"

    def __str__(self):
        return self.name
