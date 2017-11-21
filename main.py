import numpy as np
import sys

#  model: two particles and two holes
#
#     a2 ------------- (5 MeV)
#   
#   
#     a1 ------------- (2 MeV)
#   
#     ~~~~~~~~~~~~~~~~~~~
#   
#     b1 ------------- (-2 MeV)
#   
#     b2 ------------- (-4 MeV)
#    

def solveRPA(L): # L is coupling constant

    # Define energies
    Ea1 = 2
    Ea2 = 5
    Eb1 = -2
    Eb2 = -4

    # Define transition amplitudes (assuming |Qa1b1| = |(Qa1b1)*| = |Qb1a1|)
    Qa1b1 = 0.5
    Qb1a1 = Qa1b1

    Qa1b2 = 0.3;
    Qb2a1 = Qa1b2

    Qa2b1 = 0.2;
    Qb1a2 = Qa2b1

    Qa2b2 = 0.1;
    Qb2a2 = Qa2b2

    # Define RPA interaction matrix
    A = np.matrix([
        [ L*Qa1b1*Qa1b1+(Ea1-Eb1), L*Qa1b1*Qa1b2,           L*Qa1b1*Qa2b1,           L*Qa1b1*Qa2b2,           L*Qa1b1*Qb1a1,           L*Qa1b1*Qb2a1,           L*Qa1b1*Qb1a2,           L*Qa1b1*Qb2a2],
        [ L*Qa1b2*Qa1b1,           L*Qa1b2*Qa1b2+(Ea1-Eb2), L*Qa1b2*Qa2b1,           L*Qa1b2*Qa2b2,           L*Qa1b2*Qb1a1,           L*Qa1b2*Qb2a1,           L*Qa1b2*Qb1a2,           L*Qa1b2*Qb2a2],
        [ L*Qa2b1*Qa1b1,           L*Qa2b1*Qa1b2,           L*Qa2b1*Qa2b1+(Ea2-Eb1), L*Qa2b1*Qa2b2,           L*Qa2b1*Qb1a1,           L*Qa2b1*Qb2a1,           L*Qa2b1*Qb1a2,           L*Qa2b1*Qb2a2],
        [ L*Qa2b2*Qa1b1,           L*Qa2b2*Qa1b2,           L*Qa2b2*Qa2b1,           L*Qa2b2*Qa2b2+(Ea2-Eb2), L*Qa2b2*Qb1a1,           L*Qa2b2*Qb2a1,           L*Qa2b2*Qb1a2,           L*Qa2b2*Qb2a2],
        [-L*Qb1a1*Qa1b1,          -L*Qb1a1*Qa1b2,          -L*Qb1a1*Qa2b1,          -L*Qb1a1*Qa2b2,          -L*Qb1a1*Qb1a1-(Ea1-Eb1),-L*Qb1a1*Qb2a1,          -L*Qb1a1*Qb1a2,          -L*Qb1a1*Qb2a2],
        [-L*Qb2a1*Qa1b1,          -L*Qb2a1*Qa1b2,          -L*Qb2a1*Qa2b1,          -L*Qb2a1*Qa2b2,          -L*Qb2a1*Qb1a1,          -L*Qb2a1*Qb2a1-(Ea1-Eb2),-L*Qb2a1*Qb1a2,          -L*Qb2a1*Qb2a2],
        [-L*Qb1a2*Qa1b1,          -L*Qb1a2*Qa1b2,          -L*Qb1a2*Qa2b1,          -L*Qb1a2*Qa2b2,          -L*Qb1a2*Qb1a1,          -L*Qb1a2*Qb2a1,          -L*Qb1a2*Qb1a2-(Ea2-Eb1),-L*Qb1a2*Qb2a2],
        [-L*Qb2a2*Qa1b1,          -L*Qb2a2*Qa1b2,          -L*Qb2a2*Qa2b1,          -L*Qb2a2*Qa2b2,          -L*Qb2a2*Qb1a1,          -L*Qb2a2*Qb2a1,          -L*Qb2a2*Qb1a2,          -L*Qb2a2*Qb2a2-(Ea2-Eb2)]
    ])

    # calculate eigenvalues and print results
    eigenvalues = np.linalg.eigvals(A)
    for eigenvalue in eigenvalues:
        print eigenvalue

def main():

    Lvalues = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,1,2,3,4,5,6,7,8,9,10]
    for L in Lvalues:
        solveRPA(L)

main()
