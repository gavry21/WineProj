from django.db import models
from datetime import datetime

# Create your models here.
class Meta:
    db_table = 'cat'

class Wine(models.Model):
    country = models.CharField(max_length = 120,verbose_name = 'Страна')
    timestamp = models.DateTimeField(verbose_name = 'Время Добавления',default = datetime.now() )
    updated = models.DateTimeField(verbose_name = 'Время Обновления', default = datetime.now())
    id = models.AutoField(primary_key = True)
    wine_label = models.ForeignKey('Label', null = True, blank = True)
    wine_sort = models.ForeignKey('Sort', null = True, blank = True)
  
    def __unicode__(self):
        return self.country

    def __str__(self):
        return self.country  

class Label(models.Model):
    id = models.AutoField(primary_key = True) 
    name = models.CharField(max_length = 120, verbose_name = '',default = 'Название')
    year = models.CharField(max_length = 20, verbose_name = '',default = 'Год')
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Sort(models.Model):
    id = models.AutoField(primary_key = True) 
    name = models.CharField(max_length = 120, verbose_name = '',default = 'Вид')
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name        
       
class Comment(models.Model):
    id = id = models.AutoField(primary_key = True)
    comment_text = models.TextField(verbose_name = 'Комментарий',default = '')
    comment_artical = models.ForeignKey(Wine)
    def __unicode__(self):
        return self.comment_artical
    def __str__(self):
        return self.comment_artical