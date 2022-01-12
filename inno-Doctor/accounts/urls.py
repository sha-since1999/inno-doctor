from django.urls import path


from .views import (
    LogInView, ResendActivationCodeView, RemindUsernameView, SignUpView, PatientView,PatientList,  ActivateView, LogOutView,
    ChangeEmailView, ChangeEmailActivateView, ChangeProfileView, ChangePasswordView,
     RestorePasswordView, RestorePasswordDoneView, RestorePasswordConfirmView,patient_summary,Med_State,Problem_List,
Vital_signs,Social_History,past_illness
    
)

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),

    path('resend/activation-code/', ResendActivationCodeView.as_view(), name='resend_activation_code'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('patient_record_form/', PatientView, name='patient_record_form'),
    path('patient_record_list/', PatientList, name='patient_record_list'),
    path('activate/<code>/', ActivateView.as_view(), name='activate'),

    path('restore/password/', RestorePasswordView.as_view(), name='restore_password'),
    path('restore/password/done/', RestorePasswordDoneView.as_view(), name='restore_password_done'),
    path('restore/<uidb64>/<token>/', RestorePasswordConfirmView.as_view(), name='restore_password_confirm'),

    path('remind/username/', RemindUsernameView.as_view(), name='remind_username'),

    path('change/profile/', ChangeProfileView.as_view(), name='change_profile'),
    path('change/password/', ChangePasswordView.as_view(), name='change_password'),
    path('change/email/', ChangeEmailView.as_view(), name='change_email'),
    path('change/email/<code>/', ChangeEmailActivateView.as_view(), name='change_email_activation'),
    path('doctor/patient_summary/',patient_summary,name='ps'),
    path('doctor/patient_summary/med_state',Med_State,name='ms'),
    path('doctor/patient_summary/problem_list',Problem_List,name='pl'),
    path('doctor/patient_summary/vital_sign',Vital_signs,name='vs'),
    path('doctor/patient_summary/social_history',Social_History,name='sh'),
    path('doctor/patient_summary/past_illness',past_illness,name='pi'),

    
]
