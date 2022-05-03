from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
	user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
	karma = models.IntegerField(default=0, blank=True)
	def __str__(self):
		return self.user.username

class Post(models.Model):
	owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField()
	def __str__(self):
		return self.title

class Comment(models.Model):
	owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.CharField(max_length=300)
	def __str__(self):
		return self.text