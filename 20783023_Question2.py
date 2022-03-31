"""
Author: Joshua Issa
SID: 20783023
Course: PHYS 375
PS5 - Question 2
"""

import os
import numpy as np
from matplotlib import pyplot as plt

from matplotlib import rc
rc('text', usetex=True)

def part_ab(a_path="", b_path=""):
    """(a) Plots log10(R/10^3m) as a function of log10(M/Msun) over 0.01 < M/Msun < 5 and showing where
       we would find White Dwarfs, Neutron Stars, and Black Holes.
       (b) Plots on top of the figure with the average density line.
    INPUTS:
        a_path - Where to save the (a) plot.
        b_path - Where to save the (b) plot.
    OUTPUTS:
        (a) Plots the radius against the mass and identifies where to find white dwarfs, neutron stars,
        and black holes.
        (b) Plots the average density over this.
    """

    #M/Msun
    Mratio = np.linspace(0.01, 5, 10000)[1:-2] #since the range does not include 0.01 and 5.

    WD = Mratio[Mratio < 1.44] #because of the Chandrasekhar mass
    #from Ryden 18.51 where 3Msun is the accepted maximum mass of a NS
    NS = Mratio[1.44 < Mratio]
    NS = NS[NS < 3]
    BH = Mratio[3 < Mratio]

    #note that Rsun is in km and the equation is from Ryden 18.17
    Rsun = 6.955e5
    Rwd = 0.01*Rsun*np.power(WD/0.7, -1/3)

    #note that this is in km and the equation is from Ryden 18.41
    Rns = 11*np.power(NS/1.4, -1/3)

    #note that this is in km and the equation is from Ryden 18.57
    Rbh = 3*BH

    plt.title(r'$log_{10}$($\frac{R}{1 km}$) vs $log_{10}$($\frac{M}{M_\odot}$)')
    plt.ylabel(r'$log_{10}(\frac{R}{1 km})$')
    plt.xlabel(r'$log_{10}(\frac{M}{M_\odot})$')
    plt.plot(np.log10(WD), np.log10(Rwd), label='White Dwarf')
    plt.plot(np.log10(NS), np.log10(Rns), label='Neutron Star')
    plt.plot(np.log10(BH), np.log10(Rbh), label='Black Hole')

    lgd = plt.legend(bbox_to_anchor=(1.02, 1.02))

    #the region dividers
    plt.axvline(np.log10(1.44), ls='--', color='lightgrey')
    plt.axvline(np.log10(3), ls='--', color='lightgrey')

    if a_path != '':
        plt.savefig(a_path, bbox_extra_artists=(lgd,), bbox_inches='tight')
    else: plt.show()

    plt.close('all')


    rhosun = 1.5e5 * 1e9 #the density of the sun in km
    #Using DERIVED EQUATION
    Msun = 1.989e30
    Rcores = np.power(Msun*Mratio/(4*np.pi*rhosun/3), 1/3)


    plt.title(r'$log_{10}$($\frac{R}{1 km}$) vs $log_{10}$($\frac{M}{M_\odot}$)')
    plt.ylabel(r'$log_{10}(\frac{R}{1 km})$')
    plt.xlabel(r'$log_{10}(\frac{M}{M_\odot})$')
    plt.plot(np.log10(WD), np.log10(Rwd), label='White Dwarf')
    plt.plot(np.log10(NS), np.log10(Rns), label='Neutron Star')
    plt.plot(np.log10(BH), np.log10(Rbh), label='Black Hole')
    plt.plot(np.log10(Mratio), np.log10(Rcores), label='Star Cores')


    lgd = plt.legend(bbox_to_anchor=(1.02, 1.02))

    #the region dividers
    plt.axvline(np.log10(1.44), ls='--', color='lightgrey')
    plt.axvline(np.log10(3), ls='--', color='lightgrey')


    if b_path != '':
        plt.savefig(b_path, bbox_extra_artists=(lgd,), bbox_inches='tight')
    else: plt.show()

    plt.close('all')


def main():

    here = os.path.dirname(os.path.realpath(__file__))

    a_path = os.path.join(here, 'PS2-Q2a.png')
    b_path = os.path.join(here, 'PS2-Q2b.png')
    part_ab(a_path, b_path)

if __name__ == '__main__':
    main()
