#!/usr/local/crys-local/ccp4-7.0/bin/cctbx.python

import unittest

from pointless_reader import read_pointless_xml


class TestPointlessReader(unittest.TestCase):

	def setUp(self):
		pass

	
	def test_read_pointless_xml(self):
		check_results = [('cI', 197), ('oI', 23), ('tI', 97), ('mI', 5), 
				('tI', 79), ('oF', 22), ('hR', 146), ('hR', 146), 
				('mI', 5), ('hR', 146), ('hR', 146), ('mI', 5), 
				('mI', 5), ('aP', 1), ('mI', 5), ('tI', 79), 
				('tI', 97), ('mI', 5), ('cI', 211), ('tI', 79), 
				('mI', 5), ('mI', 5), ('hR', 155), ('hR', 155), 
				('hR', 155), ('mI', 5), ('tI', 97), ('hR', 155), 
				('oF', 22)]
		path = "/home/jdiaz/Collins_Tests/c5_1/1/pointless.xml"
		self.assertItemsEqual(read_pointless_xml(path), check_results)


	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=3)
