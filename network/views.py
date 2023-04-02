import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


from .models import User, Comment, Post, Follower


def index(request):
    if request.method == 'POST':
        # Create new post
        user = User.objects.get(id=request.user.id)
        content = request.POST["new_post_content"]
        new_post = Post(user_id = user, content=content)
        new_post.save()
        return HttpResponseRedirect(reverse("index"))
    else:
        # Render all the posts
        posts = Post.objects.all().order_by('-datetime')
        context = {"posts": posts}
        return render(request, "network/index.html", context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")

def profile(request, username):
    # Get the information about the requested user
    user = User.objects.get(id=request.user.id) # User who is signed in
    user_profile = User.objects.get(username=username)
    user_profile_posts = Post.objects.filter(user_id=user_profile)
    followers_count = Follower.objects.filter(following=user_profile).count()
    following_count = Follower.objects.filter(user=user_profile).count()
    # Check if user follow the user_profile
    user_following = Follower.objects.filter(user=user)
    is_following = False
    for i in user_following:
        if i.following == user_profile:
            is_following = True
            break
        else:
            is_following = False
    context = {"user_profile_posts": user_profile_posts, 
            "user_profile":user_profile,
            "user":user,
            "is_following":is_following,
            "followers_count":followers_count,
            "following_count":following_count}
    return render(request, "network/profile.html", context)

@csrf_exempt
def follow(request, user_id):
    # Manage both follow and unfullow function
    if request.method == "POST":
        user = User.objects.get(pk=request.user.id)
        data = json.loads(request.body)
        user_to_follow = User.objects.get(pk=user_id) 
        content = data["content"]
        # Following relationship exists
        follow_rel = Follower.objects.filter(user=user, following=user_to_follow)
        if follow_rel:
            follow_rel.delete()
            return JsonResponse({"message":"Unfollow successfully", "content":content, "user_to_unfollow":data["content"]})
        # Followin relationship doens't exist
        else:
            new_follower = Follower(user=user, following=user_to_follow)
            new_follower.save()
            return JsonResponse({"message":"Follow successfully", "content":content, "user_to_follow":data["content"]})
    
        
        
        