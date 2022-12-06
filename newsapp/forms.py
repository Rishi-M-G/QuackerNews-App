<<<<<<< HEAD
# ***********************Delete this later*******************************
from django import forms
from django.contrib.auth.models import User
from .models import Profile


# ***********************************************************************

# ***********************Delete this later*******************************
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
=======
from django import forms
from django.contrib.auth.models import User
from .models import Profile, Rating
>>>>>>> 7a59026 (Final Sprint)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


<<<<<<< HEAD
=======
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


>>>>>>> 7a59026 (Final Sprint)
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
<<<<<<< HEAD
        fields = ('date_of_birth', 'photo')


class NewsInput(forms.Form):
    keyword = forms.CharField()


class InviteFriendsForm(forms.Form):
    first_name = forms.CharField(max_length=225)
    email = forms.EmailField()
    to = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name','email')
# ***********************************************************************
=======
        fields = ('date_of_birth', 'photo', 'location', 'category_pref1', 'category_pref2', 'category_pref3')


class InviteForm(forms.Form):
    name = forms.CharField(max_length=100)
    from_email = forms.EmailField()
    to_email = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
>>>>>>> 7a59026 (Final Sprint)
