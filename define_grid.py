#apergrid: Calibrator grid for Apertif
#define_grid: Define and visualize grid

__author__="E.A.K. Adams"

"""
Script to define and visualize grid 
for placing calibrator observations 
across compound beam layout.
Usage:
python define_grid.py -s <sep> -o <output> -c <cboffsets>
"""

import argparse
from modules.grid_functions import *

#Argument parsing
parser = argparse.ArgumentParser(description='Define and visualize grid')
parser.add_argument('-s','--separation',default=5.0,type=float,
                    help='Separation of grid in arcminutes')
parser.add_argument('-o','--output',default='calgrid',type=str,
                    help='Base name for output files')
parser.add_argument('-c','--cboffsets',default='cb_offsets.txt',
                    help='Compound beam offsets file')
args = parser.parse_args()

#plot calibrator grid on top of compound beam layout
plot_calgrid(args.separation,args.output,args.cboffsets)
