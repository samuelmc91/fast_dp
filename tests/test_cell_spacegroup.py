#!/usr/local/crys-local/ccp4-7.0/bin/cctbx.python
'''
Author: J Diaz
Unit test to see if cell_spacegroup works
'''

import unittest
from cell_spacegroup import spacegroup_to_lattice, check_spacegroup_name, \
			    spacegroup_number_to_name, lattice_to_spacegroup, \
			    lauegroup_to_lattice, constrain_cell 


class TestCellSpacegroup(unittest.TestCase):
	
	def setUp(self):
		pass


	def test_spacegroup_to_lattice(self):
		self.assertEqual(spacegroup_to_lattice(197), 'cI')
		self.assertEqual(spacegroup_to_lattice(1), 'aP')
		self.assertEqual(spacegroup_to_lattice(5), 'mC')
		self.assertEqual(spacegroup_to_lattice(79), 'tI')
		self.assertEqual(spacegroup_to_lattice(146), 'hR')
		self.assertEqual(spacegroup_to_lattice(22), 'oF')
		self.assertEqual(spacegroup_to_lattice(23), 'oI')


	def test_lattice_to_spacegroup(self):
		self.assertEqual(lattice_to_spacegroup('aP'), 1)
		self.assertEqual(lattice_to_spacegroup('mP'), 3)
		self.assertEqual(lattice_to_spacegroup('mC'), 5)
		self.assertEqual(lattice_to_spacegroup('mI'), 5)
		self.assertEqual(lattice_to_spacegroup('oP'), 16)
		self.assertEqual(lattice_to_spacegroup('oC'), 21)
		self.assertEqual(lattice_to_spacegroup('oI'), 23)
		self.assertEqual(lattice_to_spacegroup('oF'), 22)
		self.assertEqual(lattice_to_spacegroup('tP'), 75)
		self.assertEqual(lattice_to_spacegroup('tI'), 79)
		self.assertEqual(lattice_to_spacegroup('hP'), 143)
		self.assertEqual(lattice_to_spacegroup('hR'), 146)
		self.assertEqual(lattice_to_spacegroup('hH'), 146)
		self.assertEqual(lattice_to_spacegroup('cP'), 195)
		self.assertEqual(lattice_to_spacegroup('cF'), 196)
		self.assertEqual(lattice_to_spacegroup('cI'), 197)
		

	def test_lauegroup_to_lattice(self):
		self.assertEqual(lauegroup_to_lattice('Ammm'), 'oA')
		self.assertEqual(lauegroup_to_lattice('C2/m'), 'mC')
		self.assertEqual(lauegroup_to_lattice('I2/m'), 'mI')
		self.assertEqual(lauegroup_to_lattice('Cmmm'), 'oC')
		self.assertEqual(lauegroup_to_lattice('Fm-3'), 'cF')
		self.assertEqual(lauegroup_to_lattice('Fmmm'), 'oF')
		self.assertEqual(lauegroup_to_lattice('H-3'), 'hR')
		self.assertEqual(lauegroup_to_lattice('P-1'), 'aP')
	

	def test_spacegroup_to_name(self):
		self.assertEqual(spacegroup_number_to_name(197), 'I 2 3')
		self.assertEqual(spacegroup_number_to_name(1), 'P 1')
		self.assertEqual(spacegroup_number_to_name(3), 'P 1 2 1')
		self.assertEqual(spacegroup_number_to_name(5), 'C 1 2 1')
		self.assertEqual(spacegroup_number_to_name(16), 'P 2 2 2')
		self.assertEqual(spacegroup_number_to_name(21), 'C 2 2 2')
		self.assertEqual(spacegroup_number_to_name(23), 'I 2 2 2')
		self.assertEqual(spacegroup_number_to_name(22), 'F 2 2 2')
		self.assertEqual(spacegroup_number_to_name(75), 'P 4')
		self.assertEqual(spacegroup_number_to_name(79), 'I 4')
		self.assertEqual(spacegroup_number_to_name(143), 'P 3')
		self.assertEqual(spacegroup_number_to_name(146), 'H 3')
		self.assertEqual(spacegroup_number_to_name(195), 'P 2 3')


	def test_constrain_cell(self):
		self.assertEqual(constrain_cell('a', (199.7, 200.8, 202.5, 108.0, 109.9, 109.5)), (199.7, 200.8, 202.5, 108.0, 109.9, 109.5))
		self.assertEqual(constrain_cell('m', (236.9, 326.4, 199.7, 90.3, 125.0, 89.5)), (236.9, 326.4, 199.7, 90.0, 125.0, 90.0))
		self.assertEqual(constrain_cell('m', (327.1, 231.1, 230.9, 89.9, 133.6, 89.6)), (327.1, 231.1, 230.9, 90.0, 133.6, 90.0))  
		self.assertEqual(constrain_cell('m', (231.1, 327.1, 202.5, 89.0, 124.3, 89.6)), (231.1, 327.1, 202.5, 90.0, 124.3, 90.0)) 
		self.assertEqual(constrain_cell('o', (231.1, 230.9, 236.9, 88.7, 89.4, 89.9)), (231.1, 230.9, 236.9, 90.0, 90.0, 90.0)) 
		self.assertEqual(constrain_cell('h', (332.8, 326.4, 199.7, 90.3, 90.6, 119.0)), (329.6, 329.6, 199.7, 90.0, 90.0, 120.0)) 
		self.assertEqual(constrain_cell('m', (236.9, 326.4, 204.2, 89.8, 126.8, 90.5)), (236.9, 326.4, 204.2, 90.0, 126.8, 90.0)) 
		self.assertEqual(constrain_cell('o', (231.1, 327.1, 334.6, 91.5, 90.5, 89.6)), (231.1, 327.1, 334.6, 90.0, 90.0, 90.0))
		self.assertEqual(constrain_cell('t', (230.9, 231.1, 236.9, 89.4, 88.7, 89.9)), (231.0, 231.0, 236.9, 90.0, 90.0, 90.0))
		self.assertEqual(constrain_cell('h', (327.1, 329.2, 204.2, 91.6, 88.6, 120.4)), (328.15, 328.15, 204.2, 90.0, 90.0, 120.0))
		self.assertEqual(constrain_cell('c', (230.9, 231.1, 236.9, 89.4, 88.7, 89.9)), (232.96666666666667, 232.96666666666667, 232.96666666666667, 90.0, 90.0, 90.0))
		self.assertEqual(constrain_cell('t', (236.9, 230.9, 231.1, 89.9, 89.4, 88.7)), (233.9, 233.9, 231.1, 90.0, 90.0, 90.0))
		  

	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main(verbosity=3)
