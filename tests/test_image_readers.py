#!/usr/local/crys-local/ccp4-7.0/bin/cctbx.python
import unittest

from image_readers import failover_hdf5

class TestImageReaders(unittest.TestCase):
	
	def setUp(self):
		pass


	def test_failover_hdf5(self):
		image = "/mnt/optane/hbernstein/CollinsLaccases/data/CataApo05/5/NSLS2-18_10/CataApo05_144_master.h5"
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
		results = failover_hdf5(image)
		print(results)
		self.assertDictEqual(failover_hdf5(image), meta)


	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main(verbosity=3)
