
from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Post, Comment

# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

# class PostForm(ModelForm):
#     foo = forms.CharField(widget=SummernoteWidget())

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
    
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text')
        
# class RegisterForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']
        
# class LoginForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password1']