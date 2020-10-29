import sys

class Car:
    def __init__(self, reg_number, color):
        """
        reg_number : Car's registration number
        """
        self.reg_number = reg_number
        self.color = color


class ParkingLot:
    """
    totalSlots: Total capacity of parking
    occupiedSlots: Total no of of slots full
    slots: parking array
    """
    def __init__(self):
        self.totalSlots = 0
        self.occupiedSlots = 0
        self.slots = []

    def allot_parking_lot(self, total_slots):
        self.slots = [-1] * total_slots
        self.totalSlots = total_slots
        return self.totalSlots

    def get_next_slot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park_car(self, reg_number, color):
        if self.occupiedSlots < self.totalSlots:
            slot_id = self.get_next_slot()
            self.slots[slot_id] = Car(reg_number, color)
            self.occupiedSlots = self.occupiedSlots + 1
            return slot_id + 1
        else:
            return -1

    def leave(self, slot_id):
        if self.occupiedSlots > 0 and self.slots[slot_id - 1] != -1:
            self.slots[slot_id - 1] = -1
            self.occupiedSlots = self.occupiedSlots - 1
            return True
        else:
            return False

    def status(self):
        print("Slot No.\tRegistration No.\tColour")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                print(str(i + 1) + "\t\t" + str(self.slots[i].reg_number) + "\t\t" + str(self.slots[i].color))
            else:
                continue

    def reg_no_by_color(self, color):
        list_reg_number = []
        for i in self.slots:
            if i == -1:
                continue
            if i.color == color:
                list_reg_number.append(i.reg_number)
        return list_reg_number

    def slot_no_by_reg_no(self, reg_number):

        for i in range(len(self.slots)):
            if self.slots[i].reg_number == reg_number:
                return i + 1
            else:
                continue
        return -1

    def slot_no_by_color(self, color):
        list_slot_numbers = []
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                list_slot_numbers.append(str(i + 1))
        return list_slot_numbers

    def input_functions(self, input_line):
        if input_line.startswith('create_parking_lot'):
            if len(line.split(' ')) == 2:
                n = int(line.split(' ')[1])
                res = self.allot_parking_lot(n)
                message = 'Created a parking lot with ' + str(res) + ' slots'
            else:
                message = 'Please Provide the correct arguments'
            print(message)

        elif input_line.startswith('park'):
            if len(line.split(' ')) == 3:
                reg_number = line.split(' ')[1]
                color = line.split(' ')[2]
                res = self.park_car(reg_number, color)
                if res == -1:
                    message = "Sorry, parking lot is full"
                else:
                    message = 'Allocated slot number: ' + str(res)
            else:
                message = "Please Provide car registration number and color"
            print(message)

        elif input_line.startswith('leave'):
            if len(line.split(' ')) == 2:
                leave_slot_id = int(line.split(' ')[1])
                status = self.leave(leave_slot_id)
                if status:
                    message = 'Slot number ' + str(leave_slot_id) + ' is free'
            else:
                message = "Please provide the SlotId"
            print(message)

        elif input_line.startswith('status'):
            self.status()

        elif input_line.startswith('registration_numbers_for_cars_with_colour'):
            if len(line.split(' ')) == 2:
                color = line.split(' ')[1]
                reg_nos = self.reg_no_by_color(color)
                print(', '.join(reg_nos))
            else:
                print('Please Provide the Color')

        elif input_line.startswith('slot_numbers_for_cars_with_colour'):
            if len(line.split(' ')) == 2:
                color = line.split(' ')[1]
                list_slot_number = self.slot_no_by_color(color)
                print(', '.join(list_slot_number))
            else:
                print('Please Provide the Color')

        elif input_line.startswith('slot_number_for_registration_number'):
            if len(line.split(' ')) == 2:
                reg_no = line.split(' ')[1]
                slot_no = self.slot_no_by_reg_no(reg_no)
                if slot_no == -1:
                    print("Not found")
                else:
                    print(slot_no)
            else:
                print('Please Provide the Registration Number')

        elif input_line.startswith('exit'):
            exit(0)



if __name__ == '__main__':
    parking_lot = ParkingLot()
    #File mode
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            for line in f:
                line = line.rstrip('\n')
                parking_lot.input_functions(line)
    #Interactive mode
    else:
        while True:
            line = input("$ ")
            parking_lot.input_functions(line)