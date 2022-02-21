#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid


class Appointment:
    def __init__(self, staff, patient, appointment_schedule=None):
        """
        Pseudocode:
        When created, save parameters as its attribute. After that, automatically add the object into
        the list of all appointments through the register_appointment() method.
        """

        self.id = str(uuid.uuid4())  # Object identifier
        self.type = None
        self.staff = staff
        self.patient = patient
        self.appointment_schedule = appointment_schedule  # Which appointmentSchedule object self is related
        self.register_appointment()  # Register self to AppointmentSchedule

    def register_appointment(self):
        """
        Add self to AppointmentSchedule automatically during creation.
        :return:
        """
        self.appointment_schedule.add_appointment(self)
