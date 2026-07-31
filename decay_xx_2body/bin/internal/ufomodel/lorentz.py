# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Microsoft Windows (64-bit) (July 16, 2024)
# Date: Thu 9 Jul 2026 16:42:24


from object_library import all_lorentz, Lorentz

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot
try:
   import form_factors as ForFac 
except ImportError:
   pass


UUV1 = Lorentz(name = 'UUV1',
               spins = [ -1, -1, 3 ],
               structure = 'P(3,2) + P(3,3)')

SSS1 = Lorentz(name = 'SSS1',
               spins = [ 1, 1, 1 ],
               structure = '1')

FFS1 = Lorentz(name = 'FFS1',
               spins = [ 2, 2, 1 ],
               structure = 'ProjM(2,1) + ProjP(2,1)')

FFV1 = Lorentz(name = 'FFV1',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,1)')

FFV2 = Lorentz(name = 'FFV2',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1)')

FFV3 = Lorentz(name = 'FFV3',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) - 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV4 = Lorentz(name = 'FFV4',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 2*Gamma(3,2,-1)*ProjP(-1,1)')

FFV5 = Lorentz(name = 'FFV5',
               spins = [ 2, 2, 3 ],
               structure = 'Gamma(3,2,-1)*ProjM(-1,1) + 4*Gamma(3,2,-1)*ProjP(-1,1)')

VVS1 = Lorentz(name = 'VVS1',
               spins = [ 3, 3, 1 ],
               structure = 'Metric(1,2)')

VVS2 = Lorentz(name = 'VVS2',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,3)*P(2,1) - P(-1,1)*P(-1,3)*Metric(1,2)')

VVS3 = Lorentz(name = 'VVS3',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,2)*P(2,3) - P(-1,2)*P(-1,3)*Metric(1,2)')

VVS4 = Lorentz(name = 'VVS4',
               spins = [ 3, 3, 1 ],
               structure = 'P(1,3)*P(2,1) + P(1,2)*P(2,3) - P(-1,1)*P(-1,3)*Metric(1,2) - P(-1,2)*P(-1,3)*Metric(1,2)')

VVV1 = Lorentz(name = 'VVV1',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(2,1)*Metric(1,3)')

VVV2 = Lorentz(name = 'VVV2',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(1,2)*Metric(2,3)')

VVV3 = Lorentz(name = 'VVV3',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,2)*Metric(1,2) + P(2,3)*Metric(1,3) - P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVV4 = Lorentz(name = 'VVV4',
               spins = [ 3, 3, 3 ],
               structure = 'P(3,1)*Metric(1,2) - P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) + P(2,3)*Metric(1,3) + P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

SSSS1 = Lorentz(name = 'SSSS1',
                spins = [ 1, 1, 1, 1 ],
                structure = '1')

FFVS1 = Lorentz(name = 'FFVS1',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,4)*ProjM(2,1)')

FFVS2 = Lorentz(name = 'FFVS2',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1)')

FFVS3 = Lorentz(name = 'FFVS3',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,4)*ProjP(2,1)')

FFVS4 = Lorentz(name = 'FFVS4',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,4)*ProjM(2,1) - P(3,4)*ProjP(2,1)')

FFVS5 = Lorentz(name = 'FFVS5',
                spins = [ 2, 2, 3, 1 ],
                structure = 'P(3,4)*ProjM(2,1) + P(3,4)*ProjP(2,1)')

FFVS6 = Lorentz(name = 'FFVS6',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) + P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) - P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVS7 = Lorentz(name = 'FFVS7',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVS8 = Lorentz(name = 'FFVS8',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjM(-2,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjM(-2,1) - P(-1,4)*Gamma(-1,2,-3)*Gamma(3,-3,-2)*ProjP(-2,1) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVS9 = Lorentz(name = 'FFVS9',
                spins = [ 2, 2, 3, 1 ],
                structure = '-(P(-1,4)*Gamma(-1,2,-2)*Gamma(3,-2,-3)*ProjP(-3,1)) + P(-1,4)*Gamma(-1,-3,-2)*Gamma(3,2,-3)*ProjP(-2,1)')

FFVV1 = Lorentz(name = 'FFVV1',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Metric(3,4)*ProjM(2,1)')

FFVV2 = Lorentz(name = 'FFVV2',
                spins = [ 2, 2, 3, 3 ],
                structure = 'P(4,1)*Gamma(3,2,-1)*ProjM(-1,1) - P(4,2)*Gamma(3,2,-1)*ProjM(-1,1) + P(3,1)*Gamma(4,2,-1)*ProjM(-1,1) - P(3,2)*Gamma(4,2,-1)*ProjM(-1,1)')

FFVV3 = Lorentz(name = 'FFVV3',
                spins = [ 2, 2, 3, 3 ],
                structure = 'P(4,1)*Gamma(3,2,-1)*ProjM(-1,1) + P(4,2)*Gamma(3,2,-1)*ProjM(-1,1) + P(3,1)*Gamma(4,2,-1)*ProjM(-1,1) + P(3,2)*Gamma(4,2,-1)*ProjM(-1,1)')

FFVV4 = Lorentz(name = 'FFVV4',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1)) + Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1)')

FFVV5 = Lorentz(name = 'FFVV5',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1)')

FFVV6 = Lorentz(name = 'FFVV6',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(Gamma(3,-1,-2)*Gamma(4,2,-1)*ProjM(-2,1)) + Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1)')

FFVV7 = Lorentz(name = 'FFVV7',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,3)*Gamma(-1,2,-2)*Metric(3,4)*ProjM(-2,1)) + P(4,3)*Gamma(3,2,-1)*ProjM(-1,1)')

FFVV8 = Lorentz(name = 'FFVV8',
                spins = [ 2, 2, 3, 3 ],
                structure = '-(P(-1,4)*Gamma(-1,2,-2)*Metric(3,4)*ProjM(-2,1)) + P(3,4)*Gamma(4,2,-1)*ProjM(-1,1)')

FFVV9 = Lorentz(name = 'FFVV9',
                spins = [ 2, 2, 3, 3 ],
                structure = 'Metric(3,4)*ProjP(2,1)')

FFVV10 = Lorentz(name = 'FFVV10',
                 spins = [ 2, 2, 3, 3 ],
                 structure = 'Metric(3,4)*ProjM(2,1) - Metric(3,4)*ProjP(2,1)')

FFVV11 = Lorentz(name = 'FFVV11',
                 spins = [ 2, 2, 3, 3 ],
                 structure = 'Metric(3,4)*ProjM(2,1) + Metric(3,4)*ProjP(2,1)')

FFVV12 = Lorentz(name = 'FFVV12',
                 spins = [ 2, 2, 3, 3 ],
                 structure = 'P(4,1)*Gamma(3,2,-1)*ProjP(-1,1) - P(4,2)*Gamma(3,2,-1)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-1)*ProjP(-1,1) - P(3,2)*Gamma(4,2,-1)*ProjP(-1,1)')

FFVV13 = Lorentz(name = 'FFVV13',
                 spins = [ 2, 2, 3, 3 ],
                 structure = 'P(4,1)*Gamma(3,2,-1)*ProjP(-1,1) + P(4,2)*Gamma(3,2,-1)*ProjP(-1,1) + P(3,1)*Gamma(4,2,-1)*ProjP(-1,1) + P(3,2)*Gamma(4,2,-1)*ProjP(-1,1)')

FFVV14 = Lorentz(name = 'FFVV14',
                 spins = [ 2, 2, 3, 3 ],
                 structure = '-(Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1)) + Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVV15 = Lorentz(name = 'FFVV15',
                 spins = [ 2, 2, 3, 3 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVV16 = Lorentz(name = 'FFVV16',
                 spins = [ 2, 2, 3, 3 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVV17 = Lorentz(name = 'FFVV17',
                 spins = [ 2, 2, 3, 3 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVV18 = Lorentz(name = 'FFVV18',
                 spins = [ 2, 2, 3, 3 ],
                 structure = '-(P(-1,3)*Gamma(-1,2,-2)*Metric(3,4)*ProjP(-2,1)) + P(4,3)*Gamma(3,2,-1)*ProjP(-1,1)')

FFVV19 = Lorentz(name = 'FFVV19',
                 spins = [ 2, 2, 3, 3 ],
                 structure = '-(P(-1,4)*Gamma(-1,2,-2)*Metric(3,4)*ProjP(-2,1)) + P(3,4)*Gamma(4,2,-1)*ProjP(-1,1)')

VVSS1 = Lorentz(name = 'VVSS1',
                spins = [ 3, 3, 1, 1 ],
                structure = 'Metric(1,2)')

VVSS2 = Lorentz(name = 'VVSS2',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,3)*P(2,1) + P(1,4)*P(2,1) - P(-1,1)*P(-1,3)*Metric(1,2) - P(-1,1)*P(-1,4)*Metric(1,2)')

VVSS3 = Lorentz(name = 'VVSS3',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,2)*P(2,3) + P(1,2)*P(2,4) - P(-1,2)*P(-1,3)*Metric(1,2) - P(-1,2)*P(-1,4)*Metric(1,2)')

VVSS4 = Lorentz(name = 'VVSS4',
                spins = [ 3, 3, 1, 1 ],
                structure = 'P(1,3)*P(2,1) + P(1,4)*P(2,1) + P(1,2)*P(2,3) + P(1,2)*P(2,4) - P(-1,1)*P(-1,3)*Metric(1,2) - P(-1,2)*P(-1,3)*Metric(1,2) - P(-1,1)*P(-1,4)*Metric(1,2) - P(-1,2)*P(-1,4)*Metric(1,2)')

VVVS1 = Lorentz(name = 'VVVS1',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) - P(2,1)*Metric(1,3)')

VVVS2 = Lorentz(name = 'VVVS2',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(1,2)*Metric(2,3)')

VVVS3 = Lorentz(name = 'VVVS3',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,2)*Metric(1,2) + P(2,3)*Metric(1,3) - P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVS4 = Lorentz(name = 'VVVS4',
                spins = [ 3, 3, 3, 1 ],
                structure = 'P(3,4)*Metric(1,2) + P(2,4)*Metric(1,3) + P(1,4)*Metric(2,3)')

VVVV1 = Lorentz(name = 'VVVV1',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3)')

VVVV2 = Lorentz(name = 'VVVV2',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,3)*Metric(2,4)')

VVVV3 = Lorentz(name = 'VVVV3',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(3,2)*P(4,1)*Metric(1,2) + P(3,1)*P(4,2)*Metric(1,2) - P(2,1)*P(4,2)*Metric(1,3) - P(2,1)*P(3,2)*Metric(1,4) - P(1,2)*P(4,1)*Metric(2,3) + P(-1,1)*P(-1,2)*Metric(1,4)*Metric(2,3) - P(1,2)*P(3,1)*Metric(2,4) + P(-1,1)*P(-1,2)*Metric(1,3)*Metric(2,4)')

VVVV4 = Lorentz(name = 'VVVV4',
                spins = [ 3, 3, 3, 3 ],
                structure = 'P(2,4)*P(4,3)*Metric(1,3) + P(2,3)*P(3,4)*Metric(1,4) + P(1,4)*P(4,3)*Metric(2,3) - P(-1,3)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,3)*P(3,4)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,3)*Metric(2,4) - P(1,4)*P(2,3)*Metric(3,4) - P(1,3)*P(2,4)*Metric(3,4)')

VVVV5 = Lorentz(name = 'VVVV5',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) - 2*Metric(1,2)*Metric(3,4)')

VVVV6 = Lorentz(name = 'VVVV6',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - Metric(1,2)*Metric(3,4)')

VVVV7 = Lorentz(name = 'VVVV7',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,3)*Metric(2,4) - Metric(1,2)*Metric(3,4)')

VVVV8 = Lorentz(name = 'VVVV8',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) - (Metric(1,3)*Metric(2,4))/2. - (Metric(1,2)*Metric(3,4))/2.')

VVVV9 = Lorentz(name = 'VVVV9',
                spins = [ 3, 3, 3, 3 ],
                structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVV10 = Lorentz(name = 'VVVV10',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVV11 = Lorentz(name = 'VVVV11',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3) + P(1,3)*P(3,1)*Metric(2,4) - P(-1,1)*P(-1,3)*Metric(1,3)*Metric(2,4) + P(1,2)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,2)*Metric(1,2)*Metric(3,4)')

VVVV12 = Lorentz(name = 'VVVV12',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,1)*Metric(1,2) + P(2,4)*P(4,1)*Metric(1,3) - P(2,4)*P(3,1)*Metric(1,4) - P(2,1)*P(3,4)*Metric(1,4) + P(1,4)*P(3,1)*Metric(2,4) - P(-1,1)*P(-1,4)*Metric(1,3)*Metric(2,4) + P(1,4)*P(2,1)*Metric(3,4) - P(-1,1)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV13 = Lorentz(name = 'VVVV13',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,3)*Metric(1,2) - P(-1,3)*P(-1,4)*Metric(1,2)*Metric(3,4)')

VVVV14 = Lorentz(name = 'VVVV14',
                 spins = [ 3, 3, 3, 3 ],
                 structure = 'P(3,4)*P(4,3)*Metric(1,2) + P(2,4)*P(4,2)*Metric(1,3) + P(1,4)*P(4,1)*Metric(2,3) - P(-1,1)*P(-1,4)*Metric(1,4)*Metric(2,3) - P(-1,2)*P(-1,4)*Metric(1,3)*Metric(2,4) - P(-1,3)*P(-1,4)*Metric(1,2)*Metric(3,4)')

FFVVS1 = Lorentz(name = 'FFVVS1',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Metric(3,4)*ProjM(2,1)')

FFVVS2 = Lorentz(name = 'FFVVS2',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1)')

FFVVS3 = Lorentz(name = 'FFVVS3',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Metric(3,4)*ProjP(2,1)')

FFVVS4 = Lorentz(name = 'FFVVS4',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Metric(3,4)*ProjM(2,1) - Metric(3,4)*ProjP(2,1)')

FFVVS5 = Lorentz(name = 'FFVVS5',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Metric(3,4)*ProjM(2,1) + Metric(3,4)*ProjP(2,1)')

FFVVS6 = Lorentz(name = 'FFVVS6',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) - Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) + Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVVS7 = Lorentz(name = 'FFVVS7',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVVS8 = Lorentz(name = 'FFVVS8',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVVS9 = Lorentz(name = 'FFVVS9',
                 spins = [ 2, 2, 3, 3, 1 ],
                 structure = 'Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjM(-1,1) - Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjM(-1,1) + Gamma(3,-1,-2)*Gamma(4,2,-1)*ProjP(-2,1) - Gamma(3,2,-2)*Gamma(4,-2,-1)*ProjP(-1,1)')

FFVVS10 = Lorentz(name = 'FFVVS10',
                  spins = [ 2, 2, 3, 3, 1 ],
                  structure = '-(Gamma(3,2,-1)*Gamma(4,-1,-2)*ProjP(-2,1)) + Gamma(3,-2,-1)*Gamma(4,2,-2)*ProjP(-1,1)')

FFVVV1 = Lorentz(name = 'FFVVV1',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = 'Gamma(5,2,-1)*Metric(3,4)*ProjM(-1,1) + Gamma(4,2,-1)*Metric(3,5)*ProjM(-1,1)')

FFVVV2 = Lorentz(name = 'FFVVV2',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = 'Gamma(4,2,-1)*Metric(3,5)*ProjM(-1,1) + Gamma(3,2,-1)*Metric(4,5)*ProjM(-1,1)')

FFVVV3 = Lorentz(name = 'FFVVV3',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = 'Gamma(5,2,-1)*Metric(3,4)*ProjP(-1,1) + Gamma(4,2,-1)*Metric(3,5)*ProjP(-1,1)')

FFVVV4 = Lorentz(name = 'FFVVV4',
                 spins = [ 2, 2, 3, 3, 3 ],
                 structure = 'Gamma(4,2,-1)*Metric(3,5)*ProjP(-1,1) + Gamma(3,2,-1)*Metric(4,5)*ProjP(-1,1)')

VVVSS1 = Lorentz(name = 'VVVSS1',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,1)*Metric(1,2) - P(2,1)*Metric(1,3)')

VVVSS2 = Lorentz(name = 'VVVSS2',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,1)*Metric(1,2) + P(3,2)*Metric(1,2) - P(2,1)*Metric(1,3) - P(1,2)*Metric(2,3)')

VVVSS3 = Lorentz(name = 'VVVSS3',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,2)*Metric(1,2) + P(2,3)*Metric(1,3) - P(1,2)*Metric(2,3) - P(1,3)*Metric(2,3)')

VVVSS4 = Lorentz(name = 'VVVSS4',
                 spins = [ 3, 3, 3, 1, 1 ],
                 structure = 'P(3,4)*Metric(1,2) + P(3,5)*Metric(1,2) + P(2,4)*Metric(1,3) + P(2,5)*Metric(1,3) + P(1,4)*Metric(2,3) + P(1,5)*Metric(2,3)')

VVVVS1 = Lorentz(name = 'VVVVS1',
                 spins = [ 3, 3, 3, 3, 1 ],
                 structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVVV1 = Lorentz(name = 'VVVVV1',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,2)*Metric(1,4)*Metric(2,3) - P(5,3)*Metric(1,4)*Metric(2,3) + P(4,2)*Metric(1,5)*Metric(2,3) - P(4,3)*Metric(1,5)*Metric(2,3) - P(5,1)*Metric(1,3)*Metric(2,4) + P(5,3)*Metric(1,3)*Metric(2,4) + P(3,1)*Metric(1,5)*Metric(2,4) - P(3,2)*Metric(1,5)*Metric(2,4) - P(4,1)*Metric(1,3)*Metric(2,5) + P(4,3)*Metric(1,3)*Metric(2,5) + P(3,1)*Metric(1,4)*Metric(2,5) - P(3,2)*Metric(1,4)*Metric(2,5) + P(5,1)*Metric(1,2)*Metric(3,4) - P(5,2)*Metric(1,2)*Metric(3,4) - P(2,1)*Metric(1,5)*Metric(3,4) + P(2,3)*Metric(1,5)*Metric(3,4) + P(1,2)*Metric(2,5)*Metric(3,4) - P(1,3)*Metric(2,5)*Metric(3,4) + P(4,1)*Metric(1,2)*Metric(3,5) - P(4,2)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) + P(2,3)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) - P(1,3)*Metric(2,4)*Metric(3,5)')

VVVVV2 = Lorentz(name = 'VVVVV2',
                 spins = [ 3, 3, 3, 3, 3 ],
                 structure = 'P(5,1)*Metric(1,4)*Metric(2,3) - P(5,2)*Metric(1,4)*Metric(2,3) - P(4,1)*Metric(1,5)*Metric(2,3) + P(4,5)*Metric(1,5)*Metric(2,3) + P(5,1)*Metric(1,3)*Metric(2,4) - P(5,2)*Metric(1,3)*Metric(2,4) - P(3,1)*Metric(1,5)*Metric(2,4) + P(3,5)*Metric(1,5)*Metric(2,4) + P(4,2)*Metric(1,3)*Metric(2,5) - P(4,5)*Metric(1,3)*Metric(2,5) + P(3,2)*Metric(1,4)*Metric(2,5) - P(3,5)*Metric(1,4)*Metric(2,5) + P(4,1)*Metric(1,2)*Metric(3,5) - P(4,2)*Metric(1,2)*Metric(3,5) - P(2,1)*Metric(1,4)*Metric(3,5) + P(2,5)*Metric(1,4)*Metric(3,5) + P(1,2)*Metric(2,4)*Metric(3,5) - P(1,5)*Metric(2,4)*Metric(3,5) + P(3,1)*Metric(1,2)*Metric(4,5) - P(3,2)*Metric(1,2)*Metric(4,5) - P(2,1)*Metric(1,3)*Metric(4,5) + P(2,5)*Metric(1,3)*Metric(4,5) + P(1,2)*Metric(2,3)*Metric(4,5) - P(1,5)*Metric(2,3)*Metric(4,5)')

VVVVSS1 = Lorentz(name = 'VVVVSS1',
                  spins = [ 3, 3, 3, 3, 1, 1 ],
                  structure = 'Metric(1,4)*Metric(2,3) + Metric(1,3)*Metric(2,4) + Metric(1,2)*Metric(3,4)')

VVVVVV1 = Lorentz(name = 'VVVVVV1',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) + Metric(1,5)*Metric(2,6)*Metric(3,4) - (Metric(1,6)*Metric(2,4)*Metric(3,5))/2. - (Metric(1,4)*Metric(2,6)*Metric(3,5))/2. - (Metric(1,5)*Metric(2,4)*Metric(3,6))/2. - (Metric(1,4)*Metric(2,5)*Metric(3,6))/2. - (Metric(1,6)*Metric(2,3)*Metric(4,5))/2. - (Metric(1,3)*Metric(2,6)*Metric(4,5))/2. + Metric(1,2)*Metric(3,6)*Metric(4,5) - (Metric(1,5)*Metric(2,3)*Metric(4,6))/2. - (Metric(1,3)*Metric(2,5)*Metric(4,6))/2. + Metric(1,2)*Metric(3,5)*Metric(4,6)')

VVVVVV2 = Lorentz(name = 'VVVVVV2',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,4)*Metric(3,5) + Metric(1,4)*Metric(2,6)*Metric(3,5) + Metric(1,5)*Metric(2,4)*Metric(3,6) + Metric(1,4)*Metric(2,5)*Metric(3,6) + Metric(1,6)*Metric(2,3)*Metric(4,5) + Metric(1,3)*Metric(2,6)*Metric(4,5) - 2*Metric(1,2)*Metric(3,6)*Metric(4,5) + Metric(1,5)*Metric(2,3)*Metric(4,6) + Metric(1,3)*Metric(2,5)*Metric(4,6) - 2*Metric(1,2)*Metric(3,5)*Metric(4,6) - 2*Metric(1,4)*Metric(2,3)*Metric(5,6) - 2*Metric(1,3)*Metric(2,4)*Metric(5,6)')

VVVVVV3 = Lorentz(name = 'VVVVVV3',
                  spins = [ 3, 3, 3, 3, 3, 3 ],
                  structure = 'Metric(1,6)*Metric(2,5)*Metric(3,4) - (Metric(1,5)*Metric(2,6)*Metric(3,4))/2. + Metric(1,6)*Metric(2,4)*Metric(3,5) - (Metric(1,4)*Metric(2,6)*Metric(3,5))/2. - (Metric(1,5)*Metric(2,4)*Metric(3,6))/2. - (Metric(1,4)*Metric(2,5)*Metric(3,6))/2. + Metric(1,5)*Metric(2,3)*Metric(4,6) - (Metric(1,3)*Metric(2,5)*Metric(4,6))/2. - (Metric(1,2)*Metric(3,5)*Metric(4,6))/2. + Metric(1,4)*Metric(2,3)*Metric(5,6) - (Metric(1,3)*Metric(2,4)*Metric(5,6))/2. - (Metric(1,2)*Metric(3,4)*Metric(5,6))/2.')

