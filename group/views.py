from nturl2path import url2pathname
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from .models import Group,GroupMembership
from user.models import User
from django.utils.text import slugify
from grp_post.models import GrpPost
# Create your views here.

def create(request):
    return render(request,'create.html')

def createhandler(request):
    if request.method=='POST':
        icon=request.POST['icon']
        name=request.POST['name']
        desp=request.POST['text']
        group=Group(name=name,description=desp,icon=icon)
        group.save()
        group.addmember(request.user)
        group.addadmin(request.user)
        url='/grp/view/'+group.slug
        return redirect(url)

def view(request):
    groups=Group.objects.all()
    params={'groups':groups}
    return render(request,'list.html',params)

def viewgrp(request,slug):
    grp=Group.objects.get(slug=slug)
    memberships=GroupMembership.objects.all().filter(group=grp)
    members=[membership.user for membership in memberships]
    dates=[membership.date_joined.date() for membership in memberships]
    admins=grp.grp_admins.all()
    active=[]
    for member in members:
        if member.is_active:
            active.append(member)
    params={'group':grp,'members':members,'dates':dates,'admins':admins,'active':active}
    return render(request,'view.html',params)

def joingrp(request,slug):
    grp=Group.objects.get(slug=slug)
    if request.user in grp.members.all():
        pass
    else:
        grp.addmember(request.user)
    url='/grp/view/'+slug
    return redirect(url)

def leavegrp(request,slug):
    grp=Group.objects.get(slug=slug)
    grp.removemember(request.user)
    grp.removeadmin(request.user)
    if grp.no_of_admins==0:
        memberships=grp.memberships.all()
        memberships_dates=[membership.date_joined for membership in memberships]
        first_member_date=min(memberships_dates)
        first_membership=grp.memberships.get(date_joined=first_member_date)
        first_member=first_membership.user
        grp.addadmin(first_member)
        grp.save()
    if grp.no_of_members>0:
        url='/grp/view/'+slug
    else:
        grp.delete()
        url='/grp/view/'
    return redirect(url)

def delete(request,slug):
    group=Group.objects.get(slug=slug)
    group.delete()
    url='/grp/view/'
    return redirect(url)

def joinchat(request,slug):
    group=Group.objects.get(slug=slug)
    user=request.user
    user_memberships=user.user_groups.all()
    user_groups=[user_membership.group for user_membership in user_memberships]

    grp_posts=GrpPost.objects.all().filter(group=group)
    grp_posts=grp_posts.reverse()
    user_check=[grp_post.user==request.user for grp_post in grp_posts]
    params={'group':group,'posts':grp_posts,'user_groups':user_groups}
    return render(request,'chat.html',params)

def groupchat(request,slug):
    group=Group.objects.get(slug=slug)
    message=request.POST['message']
    if message=='':
        pass
    else:
        temp_grp_post=GrpPost(user=request.user, message=message,group=group)
        temp_grp_post.save()
    url='/grp/joinchat/'+slug
    return redirect(url)

def joinchat_blank(request):
    user=request.user
    user_memberships=user.user_groups.all()
    user_groups=[user_membership.group for user_membership in user_memberships]
    params={'user_groups':user_groups}
    return render(request,'chat blank.html',params)