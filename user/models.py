from distutils.command.upload import upload
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, BaseUserManager
# Create your models here.


class CustomAccountManager(BaseUserManager):

    def create_superuser(self,username,password,first_name,email,**others):

        others.setdefault('is_staff',True)
        others.setdefault('is_superuser',True)
        others.setdefault('is_active',True)

        if others.get('is_staff') is not True:
            raise ValueError("User is not a staff.")
        
        if others.get('is_superuser') is not True:
            raise ValueError("User is not a superuser.")

        return self.create_user(username,password,first_name,email,**others)
    
    def create_user(self,username,password,first_name,email,**others):

        if not email:
            raise ValueError("Please enter a valid email.")

        email=self.normalize_email(email)
        user=self.model(email=email,username=username,first_name=first_name,**others)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser,PermissionsMixin):

    username=models.CharField(max_length=20,unique=True,primary_key=True)
    first_name=models.CharField(max_length=15)
    last_name=models.CharField(max_length=15,blank=True)
    email=models.EmailField()
    day_added=models.DateField(auto_now=True ,blank=True)
    age=models.IntegerField(blank=True,null=True)
    bio=models.CharField(max_length=100,blank=True)
    profile_pic=models.ImageField(upload_to='user/profile_pictures',blank=True,null=True)
    name=models.TextField(blank=True,null=True)

    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)

    objects = CustomAccountManager()

    USERNAME_FIELD='username'
    REQUIRED_FIELDS=['email','first_name']

    def __str__(self):
        return self.username

    def save(self,*args,**kwargs):
        self.name=self.first_name+" "+self.last_name
        super().save(*args,**kwargs)


class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    comment=models.TextField()

    def __str__(self):
        return ("Comment from "+self.user.username)


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post_img=models.ImageField(upload_to='user/posts',blank=True,null=True)
    post_caption=models.TextField()
    post_slug=models.SlugField(allow_unicode=True,blank=True)
    likers=models.ManyToManyField(User,blank=True,related_name='likers')
    no_of_likes=models.IntegerField(null=True,default=0)
    no_of_comments=models.IntegerField(null=True,default=0)
    comments=models.ManyToManyField(Comment,blank=True,null=True)

    def save(self,*args,**kwargs):
        self.post_slug=slugify(self.user.username+self.post_caption[0:5])
        super().save(*args,**kwargs)

    def __str__(self):
        return ("Post from "+self.user.username)

    def addliker(self,user):
        self.likers.add(user)
        self.no_of_likes+=1
        self.save()

    def removeliker(self,user):
        self.likers.remove(user)
        self.no_of_likes-=1
        self.save()

    def addcomment(self,comment):
        self.comments.add(comment)
        self.no_of_comments+=1
        self.save()

