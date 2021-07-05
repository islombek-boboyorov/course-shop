from django import forms
from .models import Items, Course, News, About, Subscribe, Video, Comment


class ItemsForm(forms.ModelForm):
    class Meta:
        model = Items()
        fields = "__all__"


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course()
        fields = "__all__"


class NewsForm(forms.ModelForm):
    class Meta:
        model = News()
        fields = "__all__"


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video()
        fields = "__all__"


class AboutForm(forms.ModelForm):
    class Meta:
        model = About()
        fields = "__all__"


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe()
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment()
        fields = "__all__"
