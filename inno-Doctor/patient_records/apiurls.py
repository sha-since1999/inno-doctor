from django.urls import path
from . import apiviews 
from django.conf.urls import url

from .apiviews import (
    PatientViewSet, 
    ProblemListViewSet,
    VitalSignViewSet,
    SocialHistoryViewSet,
    MedicationStatementViewSet,
    MedicationItemViewSet
)

# app_name = ' rest_api'

urlpatterns = [

     url( r'^e-prescription/$',MedicationItemViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^e-prescription/all$',MedicationItemViewSet.as_view(
        {
            'get': 'list',
        }
    )),

     url( r'^patient/$',PatientViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^patient/all$',PatientViewSet.as_view(
        {
            'get': 'list',
        }
    )),
     url( r'^problem-list/$',ProblemListViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^problem-list/all$',ProblemListViewSet.as_view(
        {
            'get': 'list',
        }
    )),
     url( r'^vital-sign/$',VitalSignViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^vital-sign/all$',VitalSignViewSet.as_view(
        {
            'get': 'list',
        }
    )),
     url( r'^social-history/$',SocialHistoryViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^social-history/all$',SocialHistoryViewSet.as_view(
        {
            'get': 'list',
        }
    )),
     url( r'^medication-statement/$',MedicationStatementViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^medication-statement/all$',MedicationStatementViewSet.as_view(
        {
            'get': 'list',
        }
    )),

    ]
