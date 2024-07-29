from django import forms
from django.contrib.auth import get_user_model
from .models import Staff, UserProfile, UserSettings
from .models import Subscription


User = get_user_model()

class UserSettingsForm(forms.ModelForm):
    class Meta:
        model = UserSettings
        fields = ['theme', 'account_privacy', 'notifications', 'app_language', 'message_settings']
        widgets = {
            'theme': forms.Select(choices=[('light', 'Light'), ('dark', 'Dark')]),
            'account_privacy': forms.Select(choices=[('public', 'Public'), ('private', 'Private')]),
            'notifications': forms.CheckboxInput(),
            'app_language': forms.Select(choices=[('en', 'English'), ('es', 'Spanish')]),
            'message_settings': forms.Select(choices=[('true', 'Enabled'), ('false', 'Disabled')]),
        }

class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['name', 'age', 'email', 'phone', 'location', 'hobby', 'gender', 'staff_id']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Staff.objects.filter(email=email).exists():
            raise forms.ValidationError("A staff member with this email already exists.")
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if Staff.objects.filter(phone=phone).exists():
            raise forms.ValidationError("A staff member with this phone number already exists.")
        return phone

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image', 'bio', 'phone_number', 'location', 'hobby', 'gender']


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['email']