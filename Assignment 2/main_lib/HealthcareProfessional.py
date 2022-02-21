#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid


class HealthcareProfessional:
    def __init__(self, name, appointment_schedule):
        self.name = name
        self.employee_number = str(uuid.uuid4())  # Object identifier
        self.appointment_schedule = appointment_schedule

    def consultation(self, appointment_id):
        # Once a consultation is done, remove the appointment from AppointmentSchedule
        self.appointment_schedule.cancel_or_remove_appointment(appointment_id)
        pass
