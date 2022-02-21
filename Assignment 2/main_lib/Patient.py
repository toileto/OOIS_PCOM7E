#!/usr/bin/python
#-*- coding: utf-8 -*-


from main_lib.Appointment import Appointment
from main_lib.Prescription import Prescription
import uuid


class Patient:
    def __init__(self, name, address, phone, appointment_schedule):
        self.name = name
        self.address = address
        self.phone = phone
        self.id = str(uuid.uuid4())  # Object identifier
        self.appointment_schedule = appointment_schedule

    def request_appointment(self, staff):
        # Create Appointment directly by passing staff, which is the doctor
        # the patient wants to consult with.
        Appointment(
            staff=staff,
            patient=self,
            appointment_schedule=self.appointment_schedule
        )

    def request_repeat(self, past_prescription):
        past_prescription_type = past_prescription.type
        past_prescription_doctor = past_prescription.doctor
        past_prescription_quantity = past_prescription.quantity
        past_prescription_dosage = past_prescription.dosage
        past_prescription_patient = past_prescription.patient

        # Check if the patient of past_prescription
        # belongs to the same patient. If its a different patient,
        # it will not create new prescription/
        if past_prescription_patient == self:
            new_prescription = Prescription(
                _type=past_prescription_type,
                patient=self,
                doctor=past_prescription_doctor,
                quantity=past_prescription_quantity,
                dosage=past_prescription_dosage
            )
            
            return new_prescription
        else:
            print("Prescription belongs to different patient...")

