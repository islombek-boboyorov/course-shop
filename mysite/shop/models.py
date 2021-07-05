from django.db import models


class Items(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "items"


class Course(models.Model):
    title = models.CharField(max_length=120, blank=False, null=True)
    price = models.PositiveIntegerField(default=0, blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "course"


class About(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    degree = models.CharField(max_length=150, blank=False, null=True)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "about"


class Subscribe(models.Model):
    email = models.EmailField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

    class Meta:
        db_table = "subscribe"


class News(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='image/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "news"


class Video(models.Model):
    title = models.CharField(max_length=120, blank=False, null=False)
    video = models.FileField(upload_to='video/%y', blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    course = models.ForeignKey(Course, blank=False, null=True, on_delete=models.SET_NULL)
    number = models.PositiveIntegerField(default=0, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "video"


class Comment(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    message = models.TextField(blank=False, null=False)
    course = models.ForeignKey(Course, blank=False, null=True, on_delete=models.SET_NULL)
    video = models.ForeignKey(Video, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "comment"
