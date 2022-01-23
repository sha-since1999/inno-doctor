# from django.test import SimpleTestCase
# from django.urls import reverse, resolve
# from accounts.views import LogInView, LogOutView, ResendActivationCodeView, SignUpView,ActivateView,RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView,RemindUsernameView, ChangeProfileView,ChangePasswordView,ChangeEmailView, ChangeEmailActivateView

# class TestUrls(SimpleTestCase):

#     def test_log_in_url_is_resolved(self):
#         url = reverse('accounts:log_in')
#         self.assertEqual(resolve(url).func.view_class, LogInView)

#     def test_log_out_url_is_resolved(self):
#         url = reverse('accounts:log_out')
#         self.assertEqual(resolve(url).func.view_class, LogOutView)
    
#     def test_resend_activatrion_code_url_is_resolved(self):
#         url = reverse('accounts:resend_activation_code')
#         self.assertEqual(resolve(url).func.view_class, ResendActivationCodeView)
    
#     def test_sign_up_url_is_resolved(self):
#         url = reverse('accounts:sign_up')
#         self.assertEqual(resolve(url).func.view_class, SignUpView)

#     def test_activate_url_is_resolved(self):
#         url = reverse('accounts:activate', args=['123'])
#         self.assertEqual(resolve(url).func.view_class, ActivateView)

#     def test_restore_password_url_is_resolved(self):
#         url = reverse('accounts:restore_password')
#         self.assertEqual(resolve(url).func.view_class, RestorePasswordView)
    
#     def test_log_out_url_is_resolved(self):
#         url = reverse('accounts:restore_password_done')
#         self.assertEqual(resolve(url).func.view_class, RestorePasswordDoneView)
    
#     def test_restore_password_done_url_is_resolved(self):
#         url = reverse('accounts:restore_password_confirm', args=['uid64', 'token'])
#         self.assertEqual(resolve(url).func.view_class, RestorePasswordConfirmView)

#     def test_remind_username_url_is_resolved(self):
#         url = reverse('accounts:remind_username')
#         self.assertEqual(resolve(url).func.view_class, RemindUsernameView)

#     def test_change_profile_url_is_resolved(self):
#         url = reverse('accounts:change_profile')
#         self.assertEqual(resolve(url).func.view_class, ChangeProfileView)
    
#     def test_change_password_url_is_resolved(self):
#         url = reverse('accounts:change_password')
#         self.assertEqual(resolve(url).func.view_class, ChangePasswordView)
    
#     def test_change_email_url_is_resolved(self):
#         url = reverse('accounts:change_email')
#         self.assertEqual(resolve(url).func.view_class, ChangeEmailView)

#     def test_change_email_activation_url_is_resolved(self):
#         url = reverse('accounts:change_email_activation', args=['123'])
#         self.assertEqual(resolve(url).func.view_class, ChangeEmailActivateView)