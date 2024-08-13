from django import forms
from mangomedia_app.models import Profile,MangoPost
from django.forms import ModelForm
class MangoPostForm(ModelForm):
    class Meta:
        model=MangoPost
        fields = ['title','post']
        widgets = {
            'title': forms.Textarea(attrs={'style':"height: 42px;"}),
            'post': forms.Textarea(attrs={'style': "height: 90px;"})
        }