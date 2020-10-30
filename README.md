# parking_system
Car Parking System using Python.


Details:-
It is a simple python program providing car parking to the N no of cars in a Parking Lot. 
There will be two attributes for car entering parking lot 1)Registration No 2) Color


Solution to the queries like:
- Registration numbers of all cars of a colour.
- Slot number in which a car with a given registration number is parked.
- Slot numbers of all slots where a car of a colour is parked.


Application can be run in two modes:
 -With input file as argument
 `python program.py  file_inputs.txt > output1`
 
 -With interactive mode
`python3 program.py`
 -Following are the commands to interact with parking lot system
  - create_parking_lot NUMBER OF SLOTS
  - park REGISTRATION NUMBER COLOR
  - leave SLOT NUMBER
  - status
  - registration_numbers_for_cars_with_colour COLOR
  - slot_numbers_for_cars_with_colour COLOR
  - slot_number_for_registration_number REGISTRATION NUMBER


For running Test Cases
'python3 tests.py'

