from django.db import models
from django.contrib.auth.models import User
from core.models import Skill, Value, City, Language, State

User._meta.get_field('email')._unique = True
User._meta.get_field('email').blank = False
User._meta.get_field('email').null = False


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    firstname = models.CharField(max_length=30, blank=True)
    lastname = models.CharField(max_length=30, blank=True)
    highested = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length = 1, choices = (('M', 'Male'),('F', 'Female')), blank= True)
    birthdate = models.DateField(null = True)
    bio = models.CharField(max_length = 350, blank = True)
    phone = models.CharField(max_length = 13, blank = True)
    city = models.ForeignKey(City, on_delete = models.SET_NULL, related_name = 'users', null=True)
    state = models.ForeignKey(State, on_delete = models.SET_NULL, related_name = 'users', null=True)
    languages = models.ManyToManyField(Language, related_name='users', blank=True)
    skills = models.ManyToManyField(Skill, related_name = 'users', blank= True)
    values = models.ManyToManyField(Value, related_name = 'users', blank =True)
    q1 = models.BooleanField(default = False)
    q2 = models.BooleanField(default = False)
    q3 = models.BooleanField(default = False)
    pic = models.ImageField(upload_to='ProfilePicture/', blank=True)
    highested = models.CharField(max_length=30, blank=True)
    institution = models.CharField(max_length=30, blank=True)
    company = models.CharField(max_length=30, blank=True)
    designation = models.CharField(max_length=30, blank=True)
    following = models.ManyToManyField(User, related_name = 'followers', blank = True, null= True)
    tandcversion = models.IntegerField(default=0)
    
    """ avatar = models.ImageField(upload_to='AvatorPicture/', blank=True) """
    timestamp = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null = True)
    last_updated_at = models.DateTimeField(auto_now=True)
    email_verified_at = models.DateTimeField(blank=True, null = True)
    deactivated_at = models.DateTimeField(blank = True, null = True)

    def followers(self):
        return User.objects.filter(profile__deactivated_at__isnull=True, profile__following__id__contains=self.user.id)

    def __str__(self):
        return self.user.__str__()

    class Meta:
        ordering = ['timestamp']


""" class Follow(models.Model):

    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='follows', related_query_name='follows')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers',related_query_name='followers')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.from_user.__str__() + "follows" + self.to_user.__str__() """
class AvatarImage(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar')
    avatar = models.ImageField(upload_to='AvatorPicture/', blank=True)


class Report(models.Model):

    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported')
    text = models.CharField(max_length=350, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.__str__()


class Ban(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bans')
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True)

    def __str__(self):
        return self.user.__str__()