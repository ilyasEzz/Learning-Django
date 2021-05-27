from captcha.fields import CaptchaField
from django import forms
from .models import Comment


class UserCommentForm(forms.ModelForm):
    author = forms.CharField(label='Автор',widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Введите свой ФИО или Логин'}))
    content = forms.CharField(label='Отзыв',widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Введите свой отзыв'}))

    class Meta:
        model = Comment
        fields = ('author', 'content', )


