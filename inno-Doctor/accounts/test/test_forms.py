from django.test import SimpleTestCase, TestCase
from accounts.forms import (SignIn, SignInViaUsernameForm, SignInViaEmailForm, SignInViaEmailOrUsernameForm,
 SignUpForm, ResendActivationCodeForm,ResendActivationCodeViaEmailForm, RestorePasswordForm,
  RestorePasswordViaEmailOrUsernameForm, ChangeProfileForm,ChangeEmailForm, RemindUsernameForm)
from django.contrib.auth import get_user_model

class TestForms(TestCase):

    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='nk8601370',
            email='nk8601370@gmail.com',
            password='nk8601370'
        )
        user.save()


    def test_signin_form_valid_data(self):
        form = SignIn(data={
            'password': 'nk8601370'
        })

        self.assertTrue(form.is_valid())

    def test_signin_form_invalid_data(self):
        form = SignIn(data={})

        self.assertFalse(form.is_valid())

    
    def test_signviausername_form_valid_data(self):
        form = SignInViaUsernameForm(data={
            'username': 'nk8601370'
        })
        self.assertTrue(form.is_valid())

    def test_signviausername_form_invalid_data(self):
        form = SignInViaUsernameForm(data={})

        self.assertFalse(form.is_valid())

    
    def test_signviaemail_form_valid_data(self):
        form = SignInViaEmailForm(data={
            'email': 'nk8601370@gmail.com'
        })

        self.assertTrue(form.is_valid())

    def test_signviaemail_form_invalid_data(self):
        form = SignInViaEmailForm(data={})

        self.assertFalse(form.is_valid())

    def test_signviaemailorusername_form_valid_data(self):
        form = SignInViaEmailOrUsernameForm(data={
            'email_or_username': 'nk8601370@gmail.com',
        })

        self.assertTrue(form.is_valid())

    def test_signviaemailorusername_form_invalid_data(self):
        form = SignInViaEmailOrUsernameForm(data={})

        self.assertFalse(form.is_valid())

    
    def test_signup_form_valid_data(self):
        form = SignUpForm(data={
            'email': 'nk8601370@gmail.com'
        })

        self.assertTrue(form.is_valid())

    def test_signup_form_invalid_data(self):
        form = SignUpForm(data={})

        self.assertFalse(form.is_valid())

    def test_resendactivationcode_form_valid_data(self):
        form = ResendActivationCodeForm(data={
            'email_or_username': 'nk8601370@gmail.com'
        })

        self.assertTrue(form.is_valid())

    def test_resendactivationcode_form_invalid_data(self):
        form = ResendActivationCodeForm(data={})

        self.assertFalse(form.is_valid())

    def test_resendactivationcodeviaemail_form_valid_data(self):
        form = ResendActivationCodeViaEmailForm(data={
            'email': 'nk8601370@gmail.com'
        })

        self.assertTrue(form.is_valid())

    def test_resendactivationcodeviaemail_form_invalid_data(self):
        form = ResendActivationCodeViaEmailForm(data={})

        self.assertFalse(form.is_valid())

    def test_restorepassword_form_valid_data(self):
        form = RestorePasswordForm(data={
            'email': 'nk8601370@gmail.com'
        })

        self.assertTrue(form.is_valid())

    def test_restorepassword_form_invalid_data(self):
        form = RestorePasswordForm(data={})

        self.assertFalse(form.is_valid())

    def test_restorepasswordviausernameoremail_form_valid_data(self):
        form = RestorePasswordViaEmailOrUsernameForm(data={
            'email_or_username': 'nk8601370@gmail.com'
        })

        self.assertTrue(form.is_valid())

    def test_restorepasswordviausernameoremail_form_invalid_data(self):
        form = RestorePasswordViaEmailOrUsernameForm(data={})

        self.assertFalse(form.is_valid())

    def test_changeprofile_form_valid_data(self):
        form = ChangeProfileForm(data={
            'first_name': 'nk8601',
            'last_name': 'kumar'
        })

        self.assertTrue(form.is_valid())

    def test_changeprofileform_form_invalid_data(self):
        form = ChangeProfileForm(data={})

        self.assertTrue(form.is_valid())

    def test_changeemail_form_valid_data(self):
        form = ChangeEmailForm(data={
            'email': 'nk8601370@gmail.com'
        })

        self.assertTrue(form.is_valid())

    def test_changeemail_form_invalid_data(self):
        form = ChangeEmailForm(data={'email': 'abcd@gmail.com'})

        self.assertFalse(form.is_valid())

    def test_remindusername_form_valid_data(self):
        form = RemindUsernameForm(data={
            'email': 'nk8601370@gmail.com'
        })

        self.assertTrue(form.is_valid())

    def test_remindusername_form_invalid_data(self):
        form = RemindUsernameForm(data={})

        self.assertFalse(form.is_valid())

