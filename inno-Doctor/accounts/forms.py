from datetime import timedelta

from django import forms
from django.forms import ValidationError
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from .models import SocialHistory
from .models import VitalSigns



class UserCacheMixin:
    user_cache = None


class SignIn(UserCacheMixin, forms.Form):
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if settings.USE_REMEMBER_ME:
            self.fields['remember_me'] = forms.BooleanField(label=_('Remember me'), required=False)

    def clean_password(self):
        password = self.cleaned_data['password']

        if not self.user_cache:
            return password

        if not self.user_cache.check_password(password):
            raise ValidationError(_('You entered an invalid password.'))

        return password


class SignInViaUsernameForm(SignIn):
    username = forms.CharField(label=_('Username'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['username', 'password', 'remember_me']
        return ['username', 'password']

    def clean_username(self):
        username = self.cleaned_data['username']

        user = User.objects.filter(username=username).first()
        if not user:
            raise ValidationError(_('You entered an invalid username.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return username


class SignInViaEmailForm(SignIn):
    email = forms.EmailField(label=_('Email'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email', 'password', 'remember_me']
        return ['email', 'password']

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return email


class SignInViaEmailOrUsernameForm(SignIn):
    email_or_username = forms.CharField(label=_('Email or Username'))

    @property
    def field_order(self):
        if settings.USE_REMEMBER_ME:
            return ['email_or_username', 'password', 'remember_me']
        return ['email_or_username', 'password']

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address or username.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return email_or_username


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = settings.SIGN_UP_FIELDS

    email = forms.EmailField(label=_('Email'), help_text=_('Required. Enter an existing email address.'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).exists()
        if user:
            raise ValidationError(_('You can not use this email address.'))

        return email


class ResendActivationCodeForm(UserCacheMixin, forms.Form):
    email_or_username = forms.CharField(label=_('Email or Username'))

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address or username.'))

        if user.is_active:
            raise ValidationError(_('This account has already been activated.'))

        activation = user.activation_set.first()
        if not activation:
            raise ValidationError(_('Activation code not found.'))

        now_with_shift = timezone.now() - timedelta(hours=24)
        if activation.created_at > now_with_shift:
            raise ValidationError(_('Activation code has already been sent. You can request a new code in 24 hours.'))

        self.user_cache = user

        return email_or_username


class ResendActivationCodeViaEmailForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_('Email'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address.'))

        if user.is_active:
            raise ValidationError(_('This account has already been activated.'))

        activation = user.activation_set.first()
        if not activation:
            raise ValidationError(_('Activation code not found.'))

        now_with_shift = timezone.now() - timedelta(hours=24)
        if activation.created_at > now_with_shift:
            raise ValidationError(_('Activation code has already been sent. You can request a new code in 24 hours.'))

        self.user_cache = user

        return email


class RestorePasswordForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_('Email'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return email


class RestorePasswordViaEmailOrUsernameForm(UserCacheMixin, forms.Form):
    email_or_username = forms.CharField(label=_('Email or Username'))

    def clean_email_or_username(self):
        email_or_username = self.cleaned_data['email_or_username']

        user = User.objects.filter(Q(username=email_or_username) | Q(email__iexact=email_or_username)).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address or username.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return email_or_username


class ChangeProfileForm(forms.Form):
    first_name = forms.CharField(label=_('First name'), max_length=30, required=False)
    last_name = forms.CharField(label=_('Last name'), max_length=150, required=False)


class ChangeEmailForm(forms.Form):
    email = forms.EmailField(label=_('Email'))

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data['email']

        if email == self.user.email:
            raise ValidationError(_('Please enter another email.'))

        user = User.objects.filter(Q(email__iexact=email) & ~Q(id=self.user.id)).exists()
        if user:
            raise ValidationError(_('You can not use this mail.'))

        return email


class RemindUsernameForm(UserCacheMixin, forms.Form):
    email = forms.EmailField(label=_('Email'))

    def clean_email(self):
        email = self.cleaned_data['email']

        user = User.objects.filter(email__iexact=email).first()
        if not user:
            raise ValidationError(_('You entered an invalid email address.'))

        if not user.is_active:
            raise ValidationError(_('This account is not active.'))

        self.user_cache = user

        return email

class VitalSignsForm(forms.ModelForm):
    class Meta:
        model = VitalSigns
        fields = ('id','ips','body_weight','height','respiration_rate','pulse_rate','body_temperature','head_circumference','pulse_oximetry','body_mass_index', 'blood_pressure_systolic','blood_pressure_diastolic')
        
        widgets={
        'id': forms.TextInput(attrs={'class':'form-control'}), 
        'ips': forms.TextInput(attrs={'class':'form-control'}),
        'body_weight' : forms.TextInput(attrs={'class':'form-control'}),
        'height' : forms.TextInput(attrs={'class':'form-control'}),
        'respiration_rate' : forms.TextInput(attrs={'class':'form-control'}),
        'pulse_rate' : forms.TextInput(attrs={'class':'form-control'}),
        'body_temperature': forms.TextInput(attrs={'class':'form-control'}),
        'head_circumference' : forms.TextInput(attrs={'class':'form-control'}),
        'pulse_oximetry' : forms.TextInput(attrs={'class':'form-control'}),
        'body_mass_index' : forms.TextInput(attrs={'class':'form-control'}), 
        'blood_pressure_systolic' : forms.TextInput(attrs={'class':'form-control'}),
        'blood_pressure_diastolic' : forms.TextInput(attrs={'class':'form-control'})
        
        }


class SocialHistoryForm(forms.ModelForm):
    class Meta:
        model = SocialHistory
        fields = ('id','ips','tobacco_smoking_status','alcohol_consumption_status','alcohol_consumption_frequency')
        
        widgets={
        'id': forms.TextInput(attrs={'class':'form-control'}),
        'ips': forms.TextInput(attrs={'class':'form-control'}),
        'tobacco_smoking_status': forms.TextInput(attrs={'class':'form-control'}),
        'alcohol_consumption_status' : forms.TextInput(attrs={'class':'form-control'}), 
        'alcohol_consumption_frequency' : forms.TextInput(attrs={'class':'form-control'})
        
        }


