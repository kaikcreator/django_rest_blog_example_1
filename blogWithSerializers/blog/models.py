from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True)
	karma = models.IntegerField(default=0, blank=True)
	def __str__(self):
		return self.user.username

class Post(models.Model):
	owner = models.ForeignKey(UserProfile)
	title = models.CharField(max_length=100)
	body = models.TextField()
	def __str__(self):
		return self.title

class Comment(models.Model):
	owner = models.ForeignKey(UserProfile)
	post = models.ForeignKey(Post)
	text = models.CharField(max_length=300)
	def __str__(self):
		return self.text

