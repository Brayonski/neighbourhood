from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime as dt

@receiver(post_save,sender=User)
def create_profile(sender, instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()


class Neighbourhood(models.Model):
    Neighbourhood_name = models.CharField(max_length=100)
    Neighbourhood_location = models.CharField(max_length=100)
    health_department = models.CharField(max_length=200,null=True)
    health_department_address = models.CharField(max_length=200,null=True)
    hospital_call_number = models.CharField(max_length=200,null=True)
    hospital_email = models.CharField(max_length=100,null=True)
    police_department = models.CharField(max_length=200,null=True)
    police_department_address = models.CharField(max_length=200,null=True)
    police_call_number = models.CharField(max_length=100,null=True)
    police_email = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Neighbourhood_name
        

class Profile(models.Model):
    user = models.OneToOneField(User)
    neighbourhood = models.ForeignKey(Neighbourhood,null=True)
    bio = models.TextField(null=True)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/',null=True)
    community = models.ForeignKey(Neighbourhood,null=True,blank=True, related_name='population')

    def __str__(self):
        return f'{self.user.username} name' 

class Business(models.Model):
    name = models.CharField(max_length=100, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood)
    image = models.ImageField(upload_to='images/')
    email = models.CharField(max_length=100, null=True)
    posted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @classmethod
    def search_by_title(cls,search_term):
        businesses = cls.objects.filter(name__icontains=search_term)
        return businesses

class Posts(models.Model):
    image = models.ImageField()
    description = models.TextField()
    neighbourhood = models.ForeignKey(Neighbourhood,null=True)
    posted_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image

class Comment(models.Model):
    text = models.TextField()
    image = models.ForeignKey(Business)
    user = models.ForeignKey(Profile)

    def __str__(self):
        return self.text

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.save() 

    @classmethod
    def find_commentimage(cls,id):
        comments = Comments.objects.filter(image__pk = id)
        return comments