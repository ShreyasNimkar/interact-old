from django.db import models
from django.utils.text import slugify
from django.utils import timezone
from user.models import User

from django import template
register=template.Library()

class Group(models.Model):
    name=models.CharField(max_length=25,unique=True)
    slug=models.SlugField(allow_unicode=True,unique=True,blank=True)
    description=models.TextField(blank=True,default='')
    grp_admins=models.ManyToManyField(User,through='GroupAdminship',related_name='admins')
    no_of_members=models.IntegerField(default=0,blank=True)
    no_of_admins=models.IntegerField(default=0,blank=True)
    members=models.ManyToManyField(User,through='GroupMembership',related_name='members')
    icon=models.ImageField(upload_to='group/grp_icons',blank=True,null=True)
    date_created=models.DateField(default=timezone.localdate(),blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

    def addmember(self, user):
        self.members.add(user)
        self.no_of_members+=1
        self.save()
    
    def removemember(self,user):
        self.members.remove(user)
        self.no_of_members-=1
        self.save()

    def addadmin(self,user):
        self.grp_admins.add(user)
        self.no_of_admins+=1
        self.save()

    def removeadmin(self,user):
        self.grp_admins.remove(user)
        self.no_of_admins-=1
        self.save()

class GroupMembership(models.Model):
    group=models.ForeignKey(Group,related_name="memberships",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)
    date_joined=models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.user.username +" of "+ self.group.name)

    class Meta:
        unique_together=[['user','group']]

class GroupAdminship(models.Model):
    group=models.ForeignKey(Group,related_name="adminships",on_delete=models.CASCADE)
    user=models.ForeignKey(User,related_name='user_admins',on_delete=models.CASCADE)
    date_made_admin=models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.user.username +", Admin of "+ self.group.name)

    class Meta:
        unique_together=[['user','group']]


