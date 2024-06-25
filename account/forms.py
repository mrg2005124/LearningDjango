from django import forms
from .models import User
from . import models


class ProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = None
        if not user.is_superuser:
            self.fields['username'].disabled = True
            self.fields['special_user'].disabled = True
            self.fields['is_author'].disabled = True


    class Meta:
        model = models.User
        fields = ['username','first_name','email', 
              'last_name', 'special_user', 'is_author']