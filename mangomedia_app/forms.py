from django.forms import ModelForm
from mangomedia_app.models import Profile,MangoPost

        
class MangoPostForm(ModelForm):
    class Meta:
        model=MangoPost
        fields = ['title','post']