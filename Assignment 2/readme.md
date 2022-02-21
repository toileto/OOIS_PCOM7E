# A. Technical Documentation
### A.1. Folder Structure
- `lib`: Contains all the classes defined by the class diagram given
- `img`: Codio's default folder, not being used by the program
- `main.ipynb`: Notebook version of the main program
- `main.py`: Python file version of the main program

### A.2. How to Run the Program
1. (_Optional_) Activate the python virtual environment included in this repository.
```commandline
source ./venv/Scripts/activate
```
2. To run the program...
   1. Execute the program by running `main.py` if you are not using Jupyter Notebook.
    ```commandline
    python main.py
    ```
   2. Otherwise, open and run all cells inside `main.ipynb`.

# B. Comments
All classes and libraries used by both `main.py` and `main.ipynb` are located inside the `lib` folder. To find detailed comments about this program, you can find those comments inside `lib` instead of `main.py` and `main.ipynb`.

There is an additional attribute that is not defined in the diagram, `id`, on each Class being added to easily identify the object in Class methods. For example, in `AppointmentSchedule` class, its only attribute is `appointments` which is the list of all `Appointment` objects that's created. Logically, after `HealthcareProfessional` object is done with an appointment, that `Appointment` object should be removed from the list of appointments - since it's already done. Thus, to make it easy to identify which `Appointment` object to remove, using an `id` will make it easier to be done.

Other than that, the only `AppointmentSchedule` object is also attached to each Class except `Prescription` class, inside their `appointment_schedule` attribute. My reason is that every Class in the diagram is having an interaction with `AppointmentSchedule`. For example, when `Doctor` is done with a consultation, it will remove the related `Appointment` object from the list of all appointments - as explained above. Or, when a patient or receptionist wants to create an `Appointment` object.

Although it's not defined in the diagram the relationship of `AppointmentSchedule` with other Classes, I think `AppointmentSchedule` should be a _shared_ object at the centre of all activity.