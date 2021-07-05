from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from shop.models import Items, Course, About, News, Video
from shop.forms import ItemsForm, CourseForm, AboutForm, NewsForm, VideoForm


def login_required_decorator(f):
    return login_required(f, login_url="login")


def dashboard_page(request):
    return render(request, 'dashboard/index.html')


def dashboard_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'dashboard/login.html')


def dashboard_logout(request):
    logout(request)
    return redirect('login')


@login_required_decorator
def item_list(request):
    items = Items.objects.all()
    ctx = {
        "items": items
    }
    return render(request, 'dashboard/items/list.html', ctx)


@login_required_decorator
def item_create(request):
    model = Items()
    form = ItemsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/items/form.html', ctx)


@login_required_decorator
def item_edit(request, pk):
    model = Items.objects.get(id=pk)
    form = ItemsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('item_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/items/form.html', ctx)


@login_required_decorator
def item_delete(request, pk):
    model = Items.objects.get(id=pk)
    model.delete()
    return redirect('item_list')


@login_required_decorator
def course_list(request):
    courses = Course.objects.all()
    ctx = {
        "courses": courses
    }
    return render(request, 'dashboard/course/list.html', ctx)


@login_required_decorator
def course_create(request):
    model = Course()
    form = CourseForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('course_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/course/form.html', ctx)


@login_required_decorator
def course_edit(request, pk):
    model = Course.objects.get(id=pk)
    form = CourseForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('course_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/course/form.html', ctx)


@login_required_decorator
def course_delete(request, pk):
    model = Course.objects.get(id=pk)
    model.delete()
    return redirect('course_list')


@login_required_decorator
def news_list(request):
    news = News.objects.all()
    ctx = {
        "news": news
    }
    return render(request, 'dashboard/news/list.html', ctx)


@login_required_decorator
def news_create(request):
    model = News()
    form = NewsForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/news/form.html', ctx)


@login_required_decorator
def news_edit(request, pk):
    model = News.objects.get(id=pk)
    form = NewsForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('news_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/news/form.html', ctx)


@login_required_decorator
def news_delete(request, pk):
    model = News.objects.get(id=pk)
    model.delete()
    return redirect('news_list')


@login_required_decorator
def about_list(request):
    abouts = About.objects.all()
    ctx = {
        "abouts": abouts
    }
    return render(request, 'dashboard/about/list.html', ctx)


@login_required_decorator
def about_create(request):
    model = About()
    form = AboutForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('about_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/about/form.html', ctx)


@login_required_decorator
def about_edit(request, pk):
    model = About.objects.get(id=pk)
    form = AboutForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('about_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/about/form.html', ctx)


@login_required_decorator
def about_delete(request, pk):
    model = About.objects.get(id=pk)
    model.delete()
    return redirect('about_list')


@login_required_decorator
def video_list(request):
    videos = Video.objects.all()
    ctx = {
        "videos": videos
    }
    return render(request, 'dashboard/video/list.html', ctx)


@login_required_decorator
def video_create(request):
    model = Video()
    form = VideoForm(request.POST, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('video_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/video/form.html', ctx)


@login_required_decorator
def video_edit(request, pk):
    model = Video.objects.get(id=pk)
    form = VideoForm(request.POST or None, request.FILES, instance=model)
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('video_list')
        else:
            print(form.errors)
    ctx = {
        "form": form,
    }
    return render(request, 'dashboard/video/form.html', ctx)


@login_required_decorator
def video_delete(request, pk):
    model = Video.objects.get(id=pk)
    model.delete()
    return redirect('video_list')


