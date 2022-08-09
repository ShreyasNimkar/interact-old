from doctest import testmod
from re import M
from tokenize import group
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from group.models import Group
from user.models import User,Comment,Post
from .models import TestModel
from .serializers import UserSerializer,GroupSerializer,PostSerializer,CommentSerializer,TestModelSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'Instructions':'Please add the following to your url to do the corresponding operation',
        'User List':'user-detail/',
        'User Detail View':'/user-detail/(username)/',
        'User Create':'/user-create',
        'User Update':'/user-update/(username)/',
        'User Delete':'/user-delete/(username)/',

        'Group List':'group-detail/',
        'Group Detail View':'/group-detail/(group_slug)/',
        'Group Create':'/group-create',
        'Group Update':'/group-update/(group_slug)/',
        'Group Delete':'/group-delete/(group_slug)/',

        'Post List':'post-detail/(username)/',
        'Post Detail View':'/post-detail/(post_slug)/',
        'Post Create':'/post-create',
        'Post Update':'/post-update/(post_slug)/',
        'Post Delete':'/post-delete/(post_slug)/',

        'Comment List':'comment-detail/',
        'Comment Detail View':'/comment-detail/(comment_id)/',
        'Comment Create':'/comment-create',
        'Comment Update':'/comment-update/(comment_id)/',
        'Comment Delete':'/comment-delete/(comment_id)/',

        'Please Note':"The Create and Update method items should be entered in form of {'name':'your name','Other_field':'Field Value'}"

    }
    return Response(api_urls)

@api_view(['GET'])
def UserList(request):
    users=User.objects.all()
    serializer=UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def GroupList(request):
    groups=Group.objects.all()
    serializer=GroupSerializer(groups, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def UserPostList(request,username):
    allposts=Post.objects.all()
    posts=[]
    for post in allposts:
        if post.user.username==username:
            posts.append(post)
    serializer=PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def CommentList(request):
    comments=Comment.objects.all()
    serializer=CommentSerializer(comments, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def UserDetail(request,username):
    user=User.objects.get(username=username)
    serializer=UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def UserCreate(request):
    serializer=UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User Successfully Created")
    else:
        return Response("Please Input Valid Data")

@api_view(['POST'])
def UserPost(request):
    serializer=UserSerializer(data=request.data)
    print("_____________Printing from here______________")
    print(serializer)
    print("_____________Printing till here______________")
    if serializer.is_valid():
        serializer.save()
        return Response("User Successfully Created")
    else:
        return Response("Please Input Valid Data")

@api_view(['POST'])
def UserUpdate(request,username):
    user=User.objects.get(username=username)
    serializer=UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("User Successfully Updated")
    else:
        return Response("Please Input Valid Data")

@api_view(['DELETE'])
def UserDelete(request,username):
    user=User.objects.get(username=username)
    user.delete()
    return Response("User Deleted!")




@api_view(['GET'])
def TestModelView(request):
    testmodels=TestModel.objects.all()
    serializer=TestModelSerializer(testmodels, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def TestModelCreate(request):
    serializer=TestModelSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response("Test Model Successfully Created")
    else:
        return Response("Please Input Valid Data")

@api_view(['DELETE'])
def TestModelDelete(request,pk):
    model=TestModel.objects.get(id=pk)
    model.delete()
    return Response("Model Deleted!")