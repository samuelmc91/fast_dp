#!/usr/local/crys-local/ccp4-7.0/bin/cctbx.python

import unittest

from scale import scale

class TestScale(unittest.TestCase):

	def setUp(self):
		pass

	def test_scale(self):
		unit_cell = (232.96666666666667, 232.96666666666667, 232.96666666666667, 90.0, 90.0, 90.0)
		meta = {'beam': (120.55726144764847, 119.44351135718689),
			'detector': 'EIGER_9M',
			'detector_class': 'eiger 9M',
			'directory': '/mnt/optane/hbernstein/CollinsLaccases/data/CataApo05/5/NSLS2-18_10',
			'distance': 200.04000666485112,
			'end': 50,
			'exposure_time': 0.05000000074505806,
			'extra_text': 'LIB=/usr/local/crys-local/ccp4-7.0/bin/../lib/eiger2cbf.so\n',
			'matching': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
			             16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
			             31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45,
			             46, 47, 48, 49, 50],
			'oscillation': (0.0, 0.20000000298023224),
			'oscillation_axis': 'Omega_I_guess',
			'phi_end': 0.20000000298023224,
			'phi_start': 0.0,
			'phi_width': 0.20000000298023224,
			'pixel': (0.07500000356230885, 0.07500000356230885),
			'saturation': 92461.0,
			'sensor': 0.44999999227002263,
			'serial_number': 0,
			'size': (3269, 3110),
			'start': 1,
			'template': 'CataApo05_1444_??????.h5',
			'wavelength': 0.9201257824897766}
		spg_num = 197
		res_high = 6.492
		res_low = 30.0
		n_jobs = 1
		n_processors = 0
		self.assertEqual(scale(unit_cell, meta, spg_num, res_high, res_low, n_jobs, n_processors), ((224.6473, 224.6473, 224.6473, 90.0, 90.0, 90.0), 'I 2 3', 4951, (1608.34, 1593.23)))

	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main(verbosity=3)
