#!/usr/bin/python
# -*- coding: utf-8 -*-


class AppointmentSchedule:
    def __init__(self):
        self.appointments = list()

    def add_appointment(self, appointment):
        # Add passed appointment to appointments list
        self.appointments.append(appointment)

    def cancel_or_remove_appointment(self, appointment_id):
        # Method to be called by doctor, or receptionist
        # to remove Appointment object, identified by appointment_id.
        for i in self.appointments:
            if i.id == appointment_id:
                self.appointments.remove(i)
        pass

    def find_availability(self):
        pass

    def print_appointment_list(self):
        print("\n#\tAppointment List ({0}):\n#".format(
            len(self.appointments)
        ))

        for i in range(0, len(self.appointments)):
            _obj = self.appointments[i]
            print("#\t--------={0}=--------".format(i + 1))
            print("#\tid: ", _obj.id)
            print("#\tpatient_name: ", _obj.patient.name)
            print("#\tstaff: ", _obj.staff.name)
            print("#\t-------------------\n#")

        print("")
