from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profileimg', 'name', 'surname', 'age', 'phone_number', 'profession', 'about_me']

    widgets = {
        'about_me': forms.Textarea(attrs={'rows': 4}),
    }