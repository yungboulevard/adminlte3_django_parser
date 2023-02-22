from django.db import models

class News(models.Model):
	tag = models.CharField('ресурс', max_length=25, default='')
	time = models.CharField('время публикации', max_length=50, default='')
	links = models.CharField('ссылки в публикации', max_length=10000, default='')
	text_content = models.TextField('публикация', max_length=10000, default='', null=True)

	def __str__(self):
		return f'{self.id} {self.tag} {self.time}'
