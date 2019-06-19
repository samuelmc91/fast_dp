#!/usr/local/crys-local/ccp4-7.0/bin/cctbx.python

import unittest

from xds_reader import read_xds_idxref_lp, read_xds_correct_lp, \
		       read_correct_lp_get_resolution


class TestXdsReader(unittest.TestCase):

	def setUp(self):
		pass


	def test_read_xds_idxref_lp(self):
		path = "/home/jdiaz/Collins_Tests/c5_1/1/IDXREF.LP"
		results = {1: (0.0, (199.7, 200.9, 202.5, 108.0, 109.9, 109.6)), 
			   197: (42.6, (233.03333333333333, 233.03333333333333, 233.03333333333333, 90.0, 90.0, 90.0)), 
			   5: (12.4, (237.1, 326.4, 199.7, 90.0, 125.1, 90.0)), 
			   79: (31.4, (231.0, 231.0, 237.1, 90.0, 90.0, 90.0)), 
  			   146: (26.8, (329.6, 329.6, 199.7, 90.0, 90.0, 120.0)), 
			   22: (29.6, (231.1, 327.3, 334.6, 90.0, 90.0, 90.0)), 
			   23: (27.0, (231.1, 230.9, 237.1, 90.0, 90.0, 90.0)), 
			   'beam centre pixels': [1608.36, 1593.09]}
		self.assertDictEqual(read_xds_idxref_lp(path), results)


	def test_read_xds_correct_lp(self):
		path="/home/jdiaz/Collins_Tests/c5_1/1/CORRECT.LP"
		results = ((224.65, 224.65, 224.65, 90.0, 90.0, 90.0), 197)
		self.assertEqual(read_xds_correct_lp(path), results)


	def test_read_correct_lp_get_resolution(self):
		path="/home/jdiaz/Collins_Tests/c5_1/1/CORRECT.LP"
		result = 6.59
		self.assertEqual(read_correct_lp_get_resolution(path), result)


	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main(verbosity=3)
