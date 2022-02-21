#!/usr/bin/python
# -*- coding: utf-8 -*-

from main_lib.HealthcareProfessional import HealthcareProfessional
from main_lib.Prescription import Prescription


class Doctor(HealthcareProfessional):
    def __init__(self, name, appointment_schedule):
        # Since Doctor inherited from HealthcareProfessional,
        # we are using super method to activate its parent
        # init method.
        super(Doctor, self).__init__(name, appointment_schedule)

    def issue_prescription(self, _type, patient, quantity, dosage):
        return Prescription(
            _type=_type,
            patient=patient,
            doctor=self,
            quantity=quantity,
            dosage=dosage
        )

