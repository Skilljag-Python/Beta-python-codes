from django.db import models

class SkillGroup(models.Model):

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Skill(models.Model):

    title = models.CharField(max_length=30)
    skill_grp = models.ForeignKey(SkillGroup,on_delete=models.CASCADE, related_name='skills')
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Value(models.Model):

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Country(models.Model):

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class State(models.Model):

    title = models.CharField(max_length=30)
    country = models.ForeignKey(Country,on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

""" class District(models.Model):

    title = models.CharField(max_length=30)
    state = models.ForeignKey(State,on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title'] """

class City(models.Model):

    title = models.CharField(max_length=30)
    state = models.ForeignKey(State,on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Language(models.Model):

    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']