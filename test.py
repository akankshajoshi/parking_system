import unittest
from my_program import ParkingLot

class TestParkingLot(unittest.TestCase):

	def test_create_parking_lot(self):
		parking_lot = ParkingLot()
		res = parking_lot.allot_parking_lot(6)
		self.assertEqual(6,res)

	def test_car_park(self):
		parking_lot = ParkingLot()
		res = parking_lot.allot_parking_lot(6)
		res = parking_lot.park_car("KA-01-HH-1234","White")
		self.assertNotEqual(-1,res)

	def test_leave(self):
		parking_lot = ParkingLot()
		res = parking_lot.allot_parking_lot(6)
		res = parking_lot.park_car("KA-01-HH-1234","White")
		res = parking_lot.leave(1)
		self.assertEqual(True,res)

	def test_reg_no_by_color(self):
		parking_lot = ParkingLot()
		res = parking_lot.allot_parking_lot(6)
		res = parking_lot.park_car("KA-01-HH-1234","White")
		res = parking_lot.park_car("KA-01-HH-9999","White")
		reg_nos = parking_lot.reg_no_by_color("White")
		self.assertIn("KA-01-HH-1234",reg_nos)
		self.assertIn("KA-01-HH-9999",reg_nos)

	def test_slot_no_by_reg_no(self):
		parking_lot = ParkingLot()
		res = parking_lot.allot_parking_lot(6)
		res = parking_lot.park_car("KA-01-HH-1234","White")
		res = parking_lot.park_car("KA-01-HH-9999","White")
		slot_no = parking_lot.slot_no_by_reg_no("KA-01-HH-9999")
		self.assertEqual(2,slot_no)

	def test_slot_no_by_color(self):
		parking_lot = ParkingLot()
		res = parking_lot.allot_parking_lot(6)
		res = parking_lot.park_car("KA-01-HH-1234","White")
		res = parking_lot.park_car("KA-01-HH-9999","White")
		slot_nos = parking_lot.slot_no_by_color("White")
		self.assertIn("1",slot_nos)
		self.assertIn("2",slot_nos)

if __name__ == '__main__':
	unittest.main()
