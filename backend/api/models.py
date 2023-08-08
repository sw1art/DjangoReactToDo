from django.db import models
from datetime import datetime

class ToDo(models.Model):
    text = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def formatted_updated_at(self):
        return self.updated_at.strftime("%H:%M %d.%m.%Y")
    
    def __str__(self):
        return f'{self.text[:60]} / Время: {self.formatted_updated_at()}'
