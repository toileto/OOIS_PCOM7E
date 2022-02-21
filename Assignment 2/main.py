import random

from lib.AppointmentSchedule import AppointmentSchedule
from lib.Appointment import Appointment
from lib.Doctor import Doctor
from lib.HealthcareProfessional import HealthcareProfessional
from lib.Nurse import Nurse
from lib.Patient import Patient
from lib.Prescription import Prescription
from lib.Receptionist import Receptionist
from pprint import pprint


def get_random_appointment(_appointment_schedule):
    """
    Custom method to get random appointment from _appointment_schedule
    :param _appointment_schedule: The AppointmentSchedule object
    :type _appointment_schedule: AppointmentSchedule
    :return: Random appointment ID
    :rtype: str
    """
    random_x = random.randint(0, len(_appointment_schedule.appointments) - 1)
    random_id = _appointment_schedule.appointments[random_x].id
    return random_id


if __name__ == '__main__':
    appointment_schedule = AppointmentSchedule()
    patient_1 = Patient(
        name='Patient 1',
        address='Address 1',
        phone='Phone 1',
        appointment_schedule=appointment_schedule
    )
    patient_2 = Patient(
        name='Patient 2',
        address='Address 2',
        phone='Phone 2',
        appointment_schedule=appointment_schedule
    )

    hp_doctor_1 = HealthcareProfessional(
        name='Doctor 1',
        appointment_schedule=appointment_schedule
    )
    hp_doctor_2 = HealthcareProfessional(
        name='Doctor 2',
        appointment_schedule=appointment_schedule
    )

    doctor_1 = Doctor(
        name='Doctor 1',
        appointment_schedule=appointment_schedule
    )

    receptionist = Receptionist(
        name='Receptionist 1',
        appointment_schedule=appointment_schedule,
    )

    # Test 1
    # Manual create appointment
    appointment_1 = Appointment(
        staff=hp_doctor_1,
        patient=patient_1,
        appointment_schedule=appointment_schedule
    )

    # Print all appointment
    appointment_schedule.print_appointment_list()

    # Test 2
    # Test creating appointment by receptionist
    receptionist.make_appointment(
        staff=hp_doctor_2,
        patient=patient_2
    )
    # Print all appointment
    appointment_schedule.print_appointment_list()

    # Test 3
    # Cancel appointment by receptionist
    receptionist.cancel_appointment(
        appointment_id=get_random_appointment(appointment_schedule)
    )

    # Print all appointment
    appointment_schedule.print_appointment_list()

    # Test 4
    # Doctor issuing prescriptions
    prescription_1 = doctor_1.issue_prescription(
        _type='Type 1',
        patient=patient_1,
        quantity=30,
        dosage=1.5
    )

    print("Doctor issuing prescriptions:")
    pprint(prescription_1.__dict__)
    print("\n")

    # Test 5
    # Request repeated prescription
    print("Request repeat prescription: ")
    repeated_prescription = patient_1.request_repeat(prescription_1)
    if repeated_prescription is not None:
        pprint({
            "type": type(repeated_prescription),
            "data": repeated_prescription.__dict__
        })
    print('\n')

    # Test 6
    # Request repeated prescription of other patient
    print("Request repeated prescription of other patient:")
    repeated_prescription = patient_2.request_repeat(prescription_1)
    if repeated_prescription is not None:
        pprint({
            "type": type(repeated_prescription),
            "data": repeated_prescription
        })
    print('\n')

    # Test 7
    # Patient request appointment
    before = len(appointment_schedule.appointments)
    patient_1.request_appointment(
        staff=doctor_1
    )
    appointment_schedule.print_appointment_list()
    after = len(appointment_schedule.appointments)
    print(
        "Before and after patient appointment request: {0} & {1}"
        .format(before, after)
    )

    # Test 8
    # After consultation, remove from appointment schedule
    before = len(appointment_schedule.appointments)
    doctor_1.consultation(get_random_appointment(appointment_schedule))
    after = len(appointment_schedule.appointments)
    print("Before and after consultation: {0} & {1}".format(
        before, after
    ))

    # Final list of all appointments
    appointment_schedule.print_appointment_list()
