from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

# Create your views here.


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_posts(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_single_post(request, id):
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
    except:
        return Response({"error": "POST NOT FOUND"})
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request, id):
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    except Post.DoesNotExist:
        return Response({"message": "Post not found"}, status=400)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_post(request, id):
    try:
        post = Post.objects.get(id=id)
        post.delete()
        return Response({"message": "Post deleted successfully"}, status=200)
    except:
        return Response({"message": "Post not deleted"})


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def get_all_comments(request, id):
    comments = Comment.objects.filter(post_id=id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def signup(request):
    try:
        username = request.data['username']
        password = request.data['password']
        user = User.objects.create_user(username=username, password=password)
        user.save()
        return Response({"message": "User Created Successfull"}, status=201)
    except:
        return Response({"error": "User already exists"}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_users(request):
    try:
        users = User.objects.all()
        li = []
        for i in users:
            li.append({
                "name": i.username
            })
        return Response(li, status=200)
    except:
        return Response({"message": "Some error occured"})
