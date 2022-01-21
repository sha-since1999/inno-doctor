import pytest
from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import medicationStatementCreate
from .conftest import (MedicationItemFactory, MedicationStatementFactory,
                       PatientFactory, )
from .models import MedicationItem, MedicationStatement
pytestmark = pytest.mark.django_db
class TestMedicationStatement(TestCase):
    def test_medication_statement_when_invalid_details(self):
        #Arrange
        aadhar_id = "698124851923"

        #Act
        response = self.client.post(
                'patient_records/patient-medication-statement/{}'.format(aadhar_id))

        #Assert
        assert response.status_code == 404
        self.assertWarnsMessage(response, 'failed to Add New E - prescription')

    # def test_medication_statement_when_valid_details(self):
    #     # Arrange
    #     patient = PatientFactory.create()
    #     aadhar_id = patient.aadhaarId
    #     medication_statement = MedicationStatementFactory.create(
    #             patient=patient)
    #     data = MedicationItemFactory.create(medication_statement=medication_statement)
    #
    #     # Act
    #     request = self.client.post(
    #             path=f"patient_records/patient-medication-statement"
    #                  f"/{aadhar_id}",
    #      data ={"items": data})
    #     # response = medicationStatementCreate(request = request, id = aadhar_id)
    #
    #     # Assert
    #     # statement = MedicationStatement.objects.filter(patient=patient)
    #     # objs = MedicationItem.objects.filter(
    #     #         medication_statement=statement).exists()
    #     # assert objs == True
    #     assert request.status_code == 200

    def test_get_medication_statement_when_invalid_details(self):
        # Arrange
        patient = PatientFactory.create()
        aadhar_id = patient.aadhaarId

        # Act
        response = self.client.get(
                'patient_records/eprescription/{}'.format(
                    aadhar_id
                    )
        )

        # Assert
        assert response.status_code == 404

    def test_get_medication_statement_when_valid_details(self):
        # Arrange
        patient = PatientFactory.create()
        aadhar_id = patient.aadhaarId
        medication_statement = MedicationStatementFactory.create(
                patient = patient
        )
        MedicationItemFactory.create(
                medication_statement = medication_statement
        )

        # Act
        response = self.client.get(
                'patient_records/eprescription/{}'.format(
                        aadhar_id
                )
        )

        # Assert
        assert response.status_code == 200
