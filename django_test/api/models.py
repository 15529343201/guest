from django.db import models

# Create your models here.
# 发布会
class Event(models.Model):
	name = models.CharField(max_length=100)
	limit = models.IntegerField()
	status = models.BooleanField()
	address = models.CharField(max_length=200)
	start_time = models.DateTimeField('events time')
	create_time = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name

# 嘉宾
class Guest(models.Model):
	event = models.ForeignKey(Event)
	realname = models.CharField(max_length=64)
	phone = models.CharField(max_length=16)
	email = models.EmailField()
	sign = models.BooleanField()
	create_time = models.DateTimeField(auto_now=True)
	class Meta:
		unique_together = ('phone', 'event')
	def __str__(self):
		return self.realname