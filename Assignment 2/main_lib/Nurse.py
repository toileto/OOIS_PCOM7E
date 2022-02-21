#!/usr/bin/python
# -*- coding: utf-8 -*-

from main_lib.HealthcareProfessional import HealthcareProfessional


class Nurse(HealthcareProfessional):
    def __init__(self, name, appointment_schedule):
        # Since Nurse inherited from HealthcareProfessional,
        # we are using super method to activate its parent
        # init method.
        super(Nurse, self).__init__(name, appointment_schedule)
    pass
