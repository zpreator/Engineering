from Stress import *

def Problem5_36():
    tauShear = TransverseShearRound(550, 0.015, 0.0075)
    sigmaAxial = AxialRound(4000, d=0.015)
    tauTorsion = TorsionalRound(25, 0.015)
    sigmax = sigmaAxial
    tauxy =tauTorsion-tauShear
    print(sigmax, tauxy)
    Pstresses = MohrsCircle2D(sigmax, 0, tauxy)
    VM = VonMises(*Pstresses)
    n = 280E6/VM
    print(n)

    tauTorsion = TorsionalRound(25, 0.015)
    sigmaBending = BendingRound(550*.1, 0.0075, 0.015)
    sigmaAxial = AxialRound(4000, d=0.015)
    sigmax = sigmaAxial + sigmaBending
    tauxy = tauTorsion
    print(sigmax, tauxy)
    Pstresses = MohrsCircle2D(sigmax, 0, tauxy)
    VM = VonMises(*Pstresses)
    n = 280E6/VM
    print(n)

Problem5_36()