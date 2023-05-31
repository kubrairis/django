from django.db import models

# Create your models here.


class Course(models.Model):
    name  = models.CharField(max_length=100, unique=True, verbose_name="Kurs Adi", help_text="Kurs adi giriniz")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='courses/%Y/%m/%d/', height_field=None, width_field=None, max_length=None, default='courses/default_course.jpg')
    date = models.DateField(auto_now=True, auto_now_add=False)
    avaliable = models.BooleanField(default=True)

    def __str__(self):
        return self.name