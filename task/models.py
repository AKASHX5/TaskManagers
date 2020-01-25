from django.db import models
from django.contrib.auth import get_user_model

user = get_user_model()


class Task(models.Model):
    created_by = models.ForeignKey(user,on_delete=models.CASCADE, related_name='created_by',default=1)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='child', on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(get_user_model(), related_name='assigned_to')

    class Meta:
        verbose_name_plural = "Tasks"
        ordering = ['name']

    def __str__(self):
        return self.name

