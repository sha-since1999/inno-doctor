from django.urls import path
from . import views 
from django.conf.urls import url

from .views import (
    InternationalPatientSummaryViewSet, 
    EPrescriptionViewSet, 
    ProblemListViewSet,
    VitalSignsViewSet,
    SocialHistoryViewSet,
    MedicationStatementViewSet
)

app_name = '    ePrescriptions'

urlpatterns = [

     url( r'^e-prescription/$',EPrescriptionViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^e-prescription/all$',EPrescriptionViewSet.as_view(
        {
            'get': 'list',
        }
    )),

     url( r'^international-patient-summary/$',InternationalPatientSummaryViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^international-patient-summary/all$',InternationalPatientSummaryViewSet.as_view(
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
     url( r'^vital-signs/$',VitalSignsViewSet.as_view(
        {
            'get': 'retrieve',
            'post': 'create',
            'put': 'update',
            'patch': 'partial_update',
        }
    ) ),
    url( r'^vital-signs/all$',VitalSignsViewSet.as_view(
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
