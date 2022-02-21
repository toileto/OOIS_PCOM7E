#!/usr/bin/python
# -*- coding: utf-8 -*-
import uuid


class Prescription:
    def __init__(self, _type, patient, doctor, quantity, dosage):
        self.type = _type
        self.patient = patient
        self.doctor = doctor
        self.quantity = quantity
        self.dosage = dosage
        self.id = str(uuid.uuid4())  # Object identifier

