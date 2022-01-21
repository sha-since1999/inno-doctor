import factory
import datetime
from .models import Patient, MedicationItem, MedicationStatement


class PatientFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Patient

    aadhaarId = factory.Sequence(lambda n: '69812485192%d' % n)
    name = factory.Sequence(lambda n: "patient_%d" % n)
    date_of_birth = '2022-10-11'
    gender = factory.Iterator(
            [("M", "Male"),
             ("F", "Female"),
             ("O", "Other")]
    )
    last_updated_on = factory.LazyFunction(datetime.datetime.utcnow)


class MedicationStatementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MedicationStatement

    patient = factory.SubFactory(PatientFactory)
    timestamp = factory.LazyFunction(datetime.datetime.utcnow)
    description = "description"


class MedicationItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MedicationItem

    medication_statement = factory.SubFactory(MedicationStatementFactory)
    medication_item = factory.Sequence(lambda n: "item_%d" % n)
    name = factory.Sequence(lambda n: "name_%d" % n)
    form = factory.Sequence(lambda n: "form_%d" % n)
    category = factory.Sequence(lambda n: "category_%d" % n)
    unit_of_prescription = factory.Sequence(lambda n: "unit_of_pres_%d" % n)
    batch_id = factory.Sequence(lambda n: "batch_%d" % n)
    expiry = '2023-03-04'
    dose_amount = factory.Sequence(lambda n: "%d" % n)
    dose_duration = factory.Sequence(lambda n: "duration_%d" % n)
    dose_unit = factory.Sequence(lambda n: "unit_%d" % n)
    dose_specific_timing = factory.LazyFunction(datetime.time)
    route = factory.Sequence(lambda n: "route_%d" % n)
    body_site = factory.Sequence(lambda n: "body_site_%d" % n)
