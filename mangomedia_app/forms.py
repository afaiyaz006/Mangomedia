from django import forms
from mangomedia_app.models import Profile,MangoPost,Comment
from django.forms import ModelForm
class MangoPostForm(forms.ModelForm):
    class Meta:
        model = MangoPost
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a comment...'}),
        }