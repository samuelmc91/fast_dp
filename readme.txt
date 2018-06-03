This is fast_dp revision 2043; it should work on Eiger data from NSLS II 
(which has a reversed rotation axis, apparently) - from the example data
provided:

tryp2s_01deg_01sec_1_001.cbf -> 900.cbf

Got:

Fast_DP installed in: /home/gw56/svn/fast_dp
Starting image: /dls/mx-scratch/gw56/tryp_0.1deg_0.1sec/tryp2s_01deg_01sec_1_001.cbf
Running on: cs04r-sc-com09-20
Number of jobs: 1
Number of cores: 0
Processing images: 1 -> 900
Phi range: 0.00 -> 90.00
Template: tryp2s_01deg_01sec_1_###.cbf
Wavelength: 0.91790
Working in: /dls/tmp/gw56/D
All autoindexing results:
Lattice      a      b      c  alpha   beta  gamma
     hP  54.20  54.20 106.20  90.00  90.00 120.00
     oC  54.20  93.90 106.20  90.00  90.00  90.00
     mC  54.20  93.90 106.20  90.00  90.00  90.00
     mP  54.20 106.20  54.20  90.00 120.00  90.00
     aP  54.20  54.20 106.20  90.00  90.00  60.00
Mosaic spread: 0.16 < 0.17 < 0.17
Happy with sg# 150
 54.20  54.20 106.20  90.00  90.00 120.00
--------------------------------------------------------------------------------
      Low resolution  28.24  28.24   1.99
     High resolution   1.94   8.68   1.94
              Rmerge  0.015  0.012  0.000
             I/sigma  32.20  85.20   4.20
        Completeness   68.7   96.8    4.9
        Multiplicity    2.5    4.3    1.0
              CC 1/2  100.0  100.0    0.0
  Anom. Completeness   55.9  100.0    0.2
  Anom. Multiplicity    1.2    2.9    1.0
   Anom. Correlation   24.9   41.0    0.0
               Nrefl  23813    840     50
             Nunique   9552    195     48
           Mid-slope  1.033
                dF/F  0.032
          dI/sig(dI)  0.804
--------------------------------------------------------------------------------
Merging point group: P 3 2 1
Unit cell:  54.16  54.16 106.12  90.00  90.00 120.00
Processing took 00h 00m 29s (29 s) [23813 reflections]
RPS: 817.0

This looks quite reasonable (was only run on one machine...)


