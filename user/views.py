import imp
import re
from xml.etree.ElementTree import Comment
from django.shortcuts import redirect, render
from .models import User,Post,Comment
from follower_following.models import Follower
# Create your views here. 

def profile(request, username):
    user=User.objects.get(username=username)
    following=user.from_user.all()
    followers=user.to_user.all()
    posts=Post.objects.all().filter(user=user)
    posts.reverse()
    memberships=user.user_groups.all()
    groups=[membership.group for membership in memberships]
    likers=[posts[i].likers.all() for i in range(len(posts))]
    comments=[posts[i].comments.all() for i in range(len(posts))]
    requesting_user_list=request.user.from_user.all()
    requesting_user_following=[requesting_user_list_item.to_user for requesting_user_list_item in requesting_user_list]
    params={'user':user,'followers':followers,'following':following,'posts':posts,'likers':likers,'comments':comments,'requesting_user_following':requesting_user_following,'groups':groups}
    return render(request,'profile.html',params)

def follow(request,username):
    from_user=request.user
    to_user=User.objects.get(username=username)
    if to_user==from_user:
        print("Cannot Follow Yourself")
    else:
        try:
            follow=Follower(from_user=from_user,to_user=to_user)
            follow.save()
        except:
            print("ALready in Follow List")
    url='/user/view/'+to_user.username
    return redirect(url)

def unfollow(request,username):
    from_user=request.user
    to_user=User.objects.get(username=username)
    follow=Follower.objects.get(from_user=from_user,to_user=to_user)
    follow.delete()
    url='/user/view/'+to_user.username
    return redirect(url)

def feed_self(request):
    user=request.user
    posts=Post.objects.all()
    following_items=user.from_user.all()
    following=[follow.to_user for follow in following_items]
    following.append(request.user)
    feed_posts=[]
    for post in posts:
        if post.user in following:
            feed_posts.append(post)
    feed_posts.reverse()
    likers=[feed_posts[i].likers.all() for i in range(len(feed_posts))]
    comments=[feed_posts[i].comments.all() for i in range(len(feed_posts))]
    params={'posts':feed_posts,'likers':likers,'comments':comments}
    return render(request,'feed_self2.html',params)

def feed_others(request,username):
    user=User.objects.get(username=username)
    posts=Post.objects.all()
    feed_posts=[]
    for post in posts:
        if post.user==user:
            feed_posts.append(post)
    feed_posts.reverse()
    params={'posts':feed_posts, 'user':username}
    return render(request,'feed_others.html',params)

def like_post(request,post_slug):
    user=request.user
    post=Post.objects.get(post_slug=post_slug)
    if user not in post.likers.all():
        post.addliker(user)
    else:
        post.removeliker(user)
    url='/user/feed/'
    return redirect(url)

def create_post(request):
    return render(request,'create_post.html')

def create_posthandler(request):
    if request.method=='POST':
        user=request.user
        post_img=request.POST['img']
        caption=request.POST['caption']
        post=Post(user=user,post_img=post_img,post_caption=caption)
        post.save()
        url='/user/feed/'
        return redirect(url)

def delete_post(request,post_slug):
    post=Post.objects.get(post_slug=post_slug)
    post.delete()
    url='/user/feed/'
    return redirect(url)

def addcomment(request,post_slug):
    user=request.user
    post=Post.objects.get(post_slug=post_slug)
    comment=request.POST['comment']
    comment_obj=Comment(user=user,comment=comment)
    comment_obj.save()
    post.addcomment(comment_obj)
    url='/user/feed/'
    return redirect(url)