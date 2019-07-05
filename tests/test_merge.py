#!/usr/local/crys-local/ccp4-7.0/bin/cctbx.python

import unittest

from merge import merge

class TestMerge(unittest.TestCase):

	def setUp(self):
		pass


	def test_merge(self):
		results = {'cchalf_overall': 0.994, 
			   'amultiplicity_inner': 1.0, 
         		   'multiplicity_outer': 1.6, 
    			   'nref_overall': 4951, 
 			   'multiplicity_overall': 1.7, 
 			   'nunique_outer': 220, 
			   'isigma_inner': 27.3, 
			   'rmeas_outer': 1.236, 
			   'nref_inner': 4, 
 			   'nunique_inner': 2, 
			   'resol_high_outer': 6.32, 
    			   'rmerge_inner': 0.0, 
		           'amultiplicity_outer': 1.2, 
			   'multiplicity_inner': 2.0, 
			   'rmerge_overall': 0.075, 
			   'rmeas_inner': 0.0, 
			   'acompleteness_outer': 22.0, 
			   'isigma_overall': 7.5, 
			   'resol_low_overall': 28.53, 
  			   'rmeas_overall': 0.105, 
			   'resol_high_inner': 28.28, 
			   'resol_low_inner': 28.53, 
			   'cchalf_inner': 0.0, 
			   'completeness_overall': 72.1, 
			   'completeness_inner': 4.5, 
			   'completeness_outer': 71.2, 
			   'nref_outer': 357, 
			   'ccanom_overall': 0.021, 
			   'isigma_outer': 0.6, 
			   'amultiplicity_overall': 0.5, 
			   'acompleteness_overall': 25.5, 
			   'cchalf_outer': 0.346, 
			   'resol_high_overall': 6.32, 
	   	           'ccanom_outer': 0.0, 
                           'ccanom_inner': 0.0, 
			   'rmerge_outer': 0.882, 
			   'acompleteness_inner': 6.1, 
			   'nunique_overall': 2948, 
			   'resol_low_outer': 6.49}
		self.assertDictEqual(merge(), results)


	def tearDown(self):
		pass


if __name__ == '__main__':
	unittest.main(verbosity=3)
