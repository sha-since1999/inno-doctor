import pytest
from django.test import TestCase
from django.test import RequestFactory
from django.urls import resolve, reverse
from patient_records.views import PatientView, PatientList
from ..test_eprescriptions.conftest import PatientFactory

pytestmark = pytest.mark.django_db
class PatientTestCase(TestCase):

    def test_patient_prescription_for_valid_case(self):
        req = RequestFactory().get(
            reverse("patient_records:patient_record_form")
            )
        response = PatientView(req)
        assert response.status_code == 200

    def test_patient_prescription_when_patient_does_not_exist_throws_error(self):
        response = self.client.get('patient_records/patient_record_form')
        assert response.status_code == 404

    def test_patient_form_url_is_resolved(self):
        url = reverse('patient_records:patient_record_form')
        self.assertEqual(resolve(url).func, PatientView)

#     def test_patient_record_when_patient_exists(self):
#         PatientFactory.create_batch(2)
#         req = RequestFactory().post(
#                 reverse("patient_records:patient_record_list"),
#                 data = {'aadharid': '698124851920', 'bdate':
#                     '2022-10-11'}
#         )
#         resp = PatientList(req)
#         assert resp.status_code == 200

#     def test_patient_prescription_when_patient_does_not_exists(
#             self
#             ):
#         #Act
#         response = self.client.post('patient_records/patient_record_list',
#                                    data={'aadharid': 1, 'bdate': '2022-10-11'})
#         #Assert
#         assert response.status_code == 404

    def test_patient_list_url_is_resolved(self):
        url = reverse('patient_records:patient_record_list')
        self.assertEqual(resolve(url).func, PatientList)
