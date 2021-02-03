from django.db import models
from django.contrib.auth.models import User
from core.models import Skill, Value, City


class Post(models.Model):

    category = models.CharField(max_length = 1, choices = (('P', 'Project'),('O', 'Opportunity'),('T', 'Thought')))
    title = models.CharField(max_length=255, blank='True')
    description = models.TextField()
    skills = models.ManyToManyField(Skill, related_name='posts', blank=True)
    values = models.ManyToManyField(Value, related_name='posts', blank= True)
    locations = models.ManyToManyField(City, related_name = 'posts', blank = True)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    deleted_at = models.DateTimeField(blank=True, null = True)

    def __str__(self):
        return str(self.id) + ':' + str(self.title)

    class Meta:

        ordering = ['timestamp']


class PostImage(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='PostImages/')

    def __str__(self):
        return str(self.id) + ': image :' + self.post.__str__()


class Interest(models.Model):

    interest = models.CharField(max_length = 1, choices = (('I', 'Interested'),('N', 'Not Interested')))
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='interests')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='interests')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.interest) + ':' + self.created_by.__str__() + ':' + self.post.__str__()

    class Meta:
        unique_together = ('post', 'created_by',)


class BookMark(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='bookmarks')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookmarks')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'BookMarked :' + self.created_by.__str__() + ':' + self.post.__str__()

    class Meta:
        unique_together = ('post', 'created_by')

class Comment (models.Model):

    text = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_by = models.ForeignKey(User,related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.post.__str__() + ':' + self.created_by.__str__() + self.id.__str__()

    class Meta:

        ordering = ['timestamp']