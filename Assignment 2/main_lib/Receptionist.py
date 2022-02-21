#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid
from main_lib.Appointment import Appointment


class Receptionist:
    def __init__(self, name, appointment_schedule):
        self.name = name
        self.employee_number = uuid.uuid4()  # Object identifier
        self.appointment_schedule = appointment_schedule

    def make_appointment(self, staff, patient):
        Appointment(
            staff=staff,
            patient=patient,
            appointment_schedule=self.appointment_schedule
        )

    def cancel_appointment(self, appointment_id):
        # Since AppointmentSchedule object is attached to each Receptionist's object
        # It is easy to remove appointment
        self.appointment_schedule.cancel_or_remove_appointment(appointment_id)
        pass

