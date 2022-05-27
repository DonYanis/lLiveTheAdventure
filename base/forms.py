from django.forms import ModelForm, fields, BooleanField,HiddenInput
from .models import FeedBack, Trip, User,Blog
from django.contrib.auth.forms import UserCreationForm


class CreateUserForm(UserCreationForm):
    create_user_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['name','email','username','phonenumber','password1','password2']

class LoginForm(UserCreationForm):
    login_user_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['email','password']  

class UserForm(ModelForm):
    update_user_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['avatar','name','username','email','bio']

class TripForm(ModelForm):
    trip_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=Trip
        fields='__all__'
        exclude=['']

class BlogForm(ModelForm):
    edit_blog = BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=Blog
        fields=['name',]

class StatusForm(ModelForm):
    edit_status=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['points','status']

class ChangeNameForm(UserCreationForm):
    change_name_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['name']

class ChangePhoneForm(UserCreationForm):
    change_phone_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['phonenumber']

class ChangeUsernameForm(UserCreationForm):
    change_username_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['username']

class ChangeEmailForm(UserCreationForm):
    change_email_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['email']

class ChangeAvatarForm(UserCreationForm):
    change_avatar_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=User
        fields=['avatar']

class FeedbackForm(ModelForm):
    feed_form=BooleanField(widget=HiddenInput, initial=True)
    class Meta:
        model=FeedBack
        fields=['body','rate']
