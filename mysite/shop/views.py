from django.shortcuts import render, redirect

from shop import servise
from shop.forms import SubscribeForm, CommentForm
from shop.models import Items, Course, Video, Comment, About, Subscribe


def index(request):
    items = Items.objects.all()
    courses = Course.objects.all()
    abouts = About.objects.all()
    model = Subscribe()
    form = SubscribeForm(request.POST,  instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            print(form.errors)
    ctx = {
        "items": items,
        "hom": "active",
        "courses": courses,
        "abouts": abouts
    }
    return render(request, 'fronted/shop/index.html', ctx)


def news(request):
    ctx = {
        "new": "active",
    }
    return render(request, 'fronted/shop/news.html', ctx)


def course(request):
    ctx = {
        "cour": "active",
    }
    return render(request, 'fronted/shop/courses.html', ctx)


def team(request):
    abouts = About.objects.all()
    ctx = {
        "abouts": abouts,
    }
    return render(request, 'fronted/shop/team.html', ctx)


def video(request, pk, pks=1):
    user = 2
    full_name = "Tom"
    courses = servise.get_course_by_id(pk)
    cour_id = courses[0]['id']
    comments = servise.get_comments(pk, pks)
    print(comments)
    videos = servise.get_course_by_id_video(pk)

    model = Comment()
    form = CommentForm(request.POST, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    ctx = {
        "comments": comments,
        "videos": videos,
        "courses": courses,
        "user": user,
        "cour_id": cour_id,
        "name": full_name,
    }
    return render(request, 'fronted/shop/unlock.html', ctx)


def about(request):
    return render(request, 'fronted/shop/team.html')
