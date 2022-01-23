from django.http import response
from django.test import TestCase, Client
from django.urls import reverse, resolve
from accounts.models import Activation
import json


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()

    def test_log_in_view(self):
        
        response = self.client.get(reverse('accounts:log_in'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/log_in.html')
    
    def test_sign_up_view(self):
        
        response = self.client.get(reverse('accounts:sign_up'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/sign_up.html')

    def test_resend_activation_code_view(self):
        
        response = self.client.get(reverse('accounts:resend_activation_code'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/resend_activation_code.html')

    def test_restore_password_view(self):
        
        response = self.client.get(reverse('accounts:restore_password'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/restore_password.html')

    def test_change_profile_view(self):
        
        response = self.client.get(reverse('accounts:change_profile'),follow=True)

        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'accounts/profile/change_profile.html')

    def test_change_email_view(self):
        
        response = self.client.get(reverse('accounts:change_email'))

        self.assertEqual(response.status_code, 302)
        #self.assertTemplateUsed(response, 'accounts/profile/change_email.html')

    def test_remind_username_view(self):
        
        response = self.client.get(reverse('accounts:remind_username'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/remind_username.html')

    def test_change_password_view(self):
        
        response = self.client.get(reverse('accounts:change_password'),follow=True)

        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'accounts/profile/change_password.html')

    def test_restore_password_confirm_view(self):
        
        response = self.client.get(reverse('accounts:restore_password_confirm',args=['uid64', 'token']))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/restore_password_confirm.html')

    def test_restore_password_done_view(self):
        
        response = self.client.get(reverse('accounts:restore_password_done'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/restore_password_done.html')

    def test_log_out_view(self):
        
        response = self.client.get(reverse('accounts:log_out'),follow=True)
    
        self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, ('accounts/log_out.html'))

    
