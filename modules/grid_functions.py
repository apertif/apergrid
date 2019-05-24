#apergrid: Calibrator grid for Apertif
#E.A.K. Adams 24/05/2019

__author__="E.A.K. Adams"

"""
Helper functions related to defining
and visualizing calibrator grid
"""

from astropy.io import ascii
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection

def plot_calgrid(separation,output,cboffsets):
    """
    Plot calibrator grid on top of compound beam pattern
    Takes separation, output base name and CB offsets file
    """
    #read cboffsets file
    cbpos = ascii.read(cboffsets)
    #open figure
    fig,ax = plt.subplots(figsize=(8,8))
    ax.axis([-2,2,-2,2])
    #set up beams
    beams = []
    r = 0.25 #beam size
    for x1, y1 in zip(cbpos['ra'], cbpos['dec']):
        circle = Circle((x1, y1), r)
        beams.append(circle)
    p = PatchCollection(beams, alpha=0.4)
    ax.add_collection(p)
    #get separations 
    if separation == None:
        sep_ra_deg = (cboffsets[22]['ra'] - cboffsets[21]['ra']) / 5. 
        sep_dec_deg = (cboffsets[21]['dec'] - cboffsets[20]['ra']) / 5.
    else:
        sep_ra_deg = separation/60.
        sep_dec_deg = separation/60.
    #set up calibrator grid
    grid=[]
    
        
    plt.savefig('{}.png'.format(output))
