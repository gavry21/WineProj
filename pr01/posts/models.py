from django.db import models
from datetime import datetime

# Create your models here.
class Meta:
    db_table = 'posts'
    
class Post(models.Model):
    title = models.CharField(max_length = 120,verbose_name = 'Заголовок')
    content = models.TextField(verbose_name = 'Контент',default = '')
    timestamp = models.DateTimeField(verbose_name = 'Время Добавления',default = datetime.now() )
    updated = models.DateTimeField(verbose_name = 'Время Обновления', default = datetime.now())
    id = models.AutoField(primary_key = True)
    post_likes = models.IntegerField(default = 0)
    genre = (('r', 'Роман'),
            ('p', 'Поэма'),
            ('rr','Рассказ'))
    genre = models.CharField(max_length = 120,verbose_name = 'Жанр',  choices = genre, default = 'r')
    post_author = models.ForeignKey('Author', null = True, blank = True)
  
    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title    

class Author(models.Model):
    id = models.AutoField(primary_key = True) 
    first_name = models.CharField(max_length = 120, verbose_name = '',default = 'Имя')
    second_name = models.CharField(max_length = 120, verbose_name = '',default = 'Фамилия')
    email = models.EmailField(verbose_name = '',default = 'email')
    def __unicode__(self):
        return self.first_name

    def __str__(self):
        return self.first_name

       
class Comment(models.Model):
    id = id = models.AutoField(primary_key = True)
    comment_text = models.TextField(verbose_name = 'Комментарий',default = '')
    comment_artical = models.ForeignKey(Post)
    def __unicode__(self):
        return self.comment_artical

    def __str__(self):
        return self.comment_artical