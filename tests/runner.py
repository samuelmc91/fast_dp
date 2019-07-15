#!/usr/local/crys-local/ccp4-7.0/bin/cctbx.python
import unittest
import sys, os

sys.path.insert(0, "/home/jdiaz/fast_dp/src")
sys.path.insert(0, "/home/jdiaz/fast_dp/lib")

import test_autoindex, test_cell_spacegroup, test_image_readers, \
		test_pointless_reader, test_xds_reader, test_integrate, \
		test_merge, test_pointgroup, test_scale

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# test_autoindex.py  test_cell_spacegroup.py  test_image_readers.py  test_pointless_reader.py  test_xds_reader.py

#suite.addTests(loader.loadTestsFromModule(test_autoindex))
suite.addTests(loader.loadTestsFromModule(test_cell_spacegroup))
suite.addTests(loader.loadTestsFromModule(test_image_readers))
suite.addTests(loader.loadTestsFromModule(test_pointless_reader))
suite.addTests(loader.loadTestsFromModule(test_xds_reader))
suite.addTests(loader.loadTestsFromModule(test_integrate))
suite.addTests(loader.loadTestsFromModule(test_merge))
suite.addTests(loader.loadTestsFromModule(test_pointgroup))
suite.addTests(loader.loadTestsFromModule(test_scale))

runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
