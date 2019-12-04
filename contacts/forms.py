from captcha.fields import CaptchaField
from django import forms
from .models import Comment


class UserCommentForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'name'}))
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Type Your Comment'}))

    class Meta:
        model = Comment
        fields = ('author', 'content', )


class GuestCommentForm(UserCommentForm):
    captcha = CaptchaField(label='Введиде текст с картинки',
                           error_messages={'invalid': 'Неправильный текст'})
