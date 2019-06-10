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
import numpy as np

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
    #get separations, in degrees
    #hard-coding calculation for 39p1 layout, could try to generalize
    ra_sep,dec_sep = get_sep_deg(separation,cbpos)
    #set up calibrator grid
    grid_xx=[]
    grid_yy=[]
    #use meshgrid for each beam
    if (separation % 2) == 0:
        extra = 1
    else:
        extra = 0
    for b in range(40):
        xvalues = (np.arange(separation+extra) - np.floor((separation+extra) / 2.))*ra_sep + cbpos['ra'][b]
        yvalues = (np.arange(separation+extra) - np.floor((separation+extra) / 2.))*dec_sep + cbpos['dec'][b]
        #print(xvalues)
        xx, yy = np.meshgrid(xvalues, yvalues)
        grid_xx.append(xx)
        grid_yy.append(yy)
        ax.scatter(xx,yy)
        
    plt.savefig('{}.png'.format(output))
    
def get_sep_deg(separation,cbpos):
    #would like to generalize this, but can't find a good way
    #CB0 causes issues, as does offset nature of rows in RA from each other
    ra_cb_sep = cbpos['ra'][20]-cbpos['ra'][19]
    dec_cb_sep = cbpos['dec'][21]-cbpos['dec'][20]
    ra_sep = ra_cb_sep / separation
    dec_sep = dec_cb_sep / separation
    print(ra_cb_sep,dec_cb_sep)
    print(ra_sep,dec_sep)
    return ra_sep,dec_sep
                       
