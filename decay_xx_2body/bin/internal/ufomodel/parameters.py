# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Microsoft Windows (64-bit) (July 16, 2024)
# Date: Thu 9 Jul 2026 16:42:24



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
cabi = Parameter(name = 'cabi',
                 nature = 'external',
                 type = 'real',
                 value = 0.227736,
                 texname = '\\theta _c',
                 lhablock = 'CKMBLOCK',
                 lhacode = [ 1 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymdo = Parameter(name = 'ymdo',
                 nature = 'external',
                 type = 'real',
                 value = 0.00504,
                 texname = '\\text{ymdo}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 1 ])

ymup = Parameter(name = 'ymup',
                 nature = 'external',
                 type = 'real',
                 value = 0.00255,
                 texname = '\\text{ymup}',
                 lhablock = 'YUKAWA',
                 lhacode = [ 2 ])

yms = Parameter(name = 'yms',
                nature = 'external',
                type = 'real',
                value = 0.101,
                texname = '\\text{yms}',
                lhablock = 'YUKAWA',
                lhacode = [ 3 ])

ymc = Parameter(name = 'ymc',
                nature = 'external',
                type = 'real',
                value = 1.27,
                texname = '\\text{ymc}',
                lhablock = 'YUKAWA',
                lhacode = [ 4 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

yme = Parameter(name = 'yme',
                nature = 'external',
                type = 'real',
                value = 0.000511,
                texname = '\\text{yme}',
                lhablock = 'YUKAWA',
                lhacode = [ 11 ])

ymm = Parameter(name = 'ymm',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{ymm}',
                lhablock = 'YUKAWA',
                lhacode = [ 13 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

LamX = Parameter(name = 'LamX',
                 nature = 'external',
                 type = 'real',
                 value = 1000.,
                 texname = '\\Lambda _X',
                 lhablock = 'FRBlock',
                 lhacode = [ 1 ])

CXB = Parameter(name = 'CXB',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'C_{\\text{XB}}',
                lhablock = 'FRBlock',
                lhacode = [ 2 ])

CXe = Parameter(name = 'CXe',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'C_{\\text{Xe}}',
                lhablock = 'FRBlock',
                lhacode = [ 3 ])

CXl = Parameter(name = 'CXl',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'C_{\\text{Xl}}',
                lhablock = 'FRBlock',
                lhacode = [ 4 ])

CXq = Parameter(name = 'CXq',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'C_{\\text{Xq}}',
                lhablock = 'FRBlock',
                lhacode = [ 5 ])

CXd = Parameter(name = 'CXd',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'C_{\\text{Xd}}',
                lhablock = 'FRBlock',
                lhacode = [ 6 ])

CXu = Parameter(name = 'CXu',
                nature = 'external',
                type = 'real',
                value = 1.,
                texname = 'C_{\\text{Xu}}',
                lhablock = 'FRBlock',
                lhacode = [ 7 ])

CDHieLX = Parameter(name = 'CDHieLX',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = 'C_{\\text{DHieLX}}',
                    lhablock = 'FRBlock',
                    lhacode = [ 8 ])

CDHiesLX = Parameter(name = 'CDHiesLX',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = 'C_{\\text{DHiesLX}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 9 ])

CDHidQX = Parameter(name = 'CDHidQX',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = 'C_{\\text{DHidQX}}',
                    lhablock = 'FRBlock',
                    lhacode = [ 10 ])

CDHidsQX = Parameter(name = 'CDHidsQX',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = 'C_{\\text{DHidsQX}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 11 ])

CDHiQuX = Parameter(name = 'CDHiQuX',
                    nature = 'external',
                    type = 'real',
                    value = 1.,
                    texname = 'C_{\\text{DHiQuX}}',
                    lhablock = 'FRBlock',
                    lhacode = [ 12 ])

CDHiQsuX = Parameter(name = 'CDHiQsuX',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = 'C_{\\text{DHiQsuX}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 13 ])

CDHieLXI = Parameter(name = 'CDHieLXI',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = 'C_{\\text{DHieLXI}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 14 ])

CDHiesLXI = Parameter(name = 'CDHiesLXI',
                      nature = 'external',
                      type = 'real',
                      value = 1.,
                      texname = 'C_{\\text{DHiesLXI}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 15 ])

CDHidQXI = Parameter(name = 'CDHidQXI',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = 'C_{\\text{DHidQXI}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 16 ])

CDHidsQXI = Parameter(name = 'CDHidsQXI',
                      nature = 'external',
                      type = 'real',
                      value = 1.,
                      texname = 'C_{\\text{DHidsQXI}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 17 ])

CDHiQuXI = Parameter(name = 'CDHiQuXI',
                     nature = 'external',
                     type = 'real',
                     value = 1.,
                     texname = 'C_{\\text{DHiQuXI}}',
                     lhablock = 'FRBlock',
                     lhacode = [ 18 ])

CDHiQsuXI = Parameter(name = 'CDHiQsuXI',
                      nature = 'external',
                      type = 'real',
                      value = 1.,
                      texname = 'C_{\\text{DHiQsuXI}}',
                      lhablock = 'FRBlock',
                      lhacode = [ 19 ])

CXH3I = Parameter(name = 'CXH3I',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'C_{\\text{XH3I}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 20 ])

CXH4I = Parameter(name = 'CXH4I',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'C_{\\text{XH4I}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 21 ])

CXfLI = Parameter(name = 'CXfLI',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'C_{\\text{XfLI}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 22 ])

CXfdI = Parameter(name = 'CXfdI',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'C_{\\text{XfdI}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 23 ])

CXfuI = Parameter(name = 'CXfuI',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'C_{\\text{XfuI}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 24 ])

CXfQI = Parameter(name = 'CXfQI',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'C_{\\text{XfQI}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 25 ])

CXHiB = Parameter(name = 'CXHiB',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'C_{\\text{XHiB}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 26 ])

CXHiBI = Parameter(name = 'CXHiBI',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = 'C_{\\text{XHiBI}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 27 ])

CXHiX = Parameter(name = 'CXHiX',
                  nature = 'external',
                  type = 'real',
                  value = 1.,
                  texname = 'C_{\\text{XHiX}}',
                  lhablock = 'FRBlock',
                  lhacode = [ 28 ])

CXHiXI = Parameter(name = 'CXHiXI',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = 'C_{\\text{XHiXI}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 29 ])

CXB2 = Parameter(name = 'CXB2',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XB2}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 30 ])

CXB3 = Parameter(name = 'CXB3',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XB2}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 31 ])

CXW2 = Parameter(name = 'CXW2',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XW2}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 32 ])

CH2X2B = Parameter(name = 'CH2X2B',
                   nature = 'external',
                   type = 'real',
                   value = 1.,
                   texname = 'C_{\\text{H2X2B}}',
                   lhablock = 'FRBlock',
                   lhacode = [ 33 ])

CXH2 = Parameter(name = 'CXH2',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XH2}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 34 ])

CXH3 = Parameter(name = 'CXH3',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XH3}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 35 ])

CXH4 = Parameter(name = 'CXH4',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XH4}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 36 ])

CXB4 = Parameter(name = 'CXB4',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XB4}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 37 ])

CXfL = Parameter(name = 'CXfL',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XfL}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 38 ])

CXfd = Parameter(name = 'CXfd',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{Xfd}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 39 ])

CXfu = Parameter(name = 'CXfu',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{Xfu}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 40 ])

CXfQ = Parameter(name = 'CXfQ',
                 nature = 'external',
                 type = 'real',
                 value = 1.,
                 texname = 'C_{\\text{XfQ}}',
                 lhablock = 'FRBlock',
                 lhacode = [ 41 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MU = Parameter(name = 'MU',
               nature = 'external',
               type = 'real',
               value = 0.00255,
               texname = 'M',
               lhablock = 'MASS',
               lhacode = [ 2 ])

MC = Parameter(name = 'MC',
               nature = 'external',
               type = 'real',
               value = 1.27,
               texname = '\\text{MC}',
               lhablock = 'MASS',
               lhacode = [ 4 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MD = Parameter(name = 'MD',
               nature = 'external',
               type = 'real',
               value = 0.00504,
               texname = '\\text{MD}',
               lhablock = 'MASS',
               lhacode = [ 1 ])

MS = Parameter(name = 'MS',
               nature = 'external',
               type = 'real',
               value = 0.101,
               texname = '\\text{MS}',
               lhablock = 'MASS',
               lhacode = [ 3 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

MX = Parameter(name = 'MX',
               nature = 'external',
               type = 'real',
               value = 10.,
               texname = '\\text{MX}',
               lhablock = 'MASS',
               lhacode = [ 9000002 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

WX = Parameter(name = 'WX',
               nature = 'external',
               type = 'real',
               value = 0.,
               texname = '\\text{WX}',
               lhablock = 'DECAY',
               lhacode = [ 9000002 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

CKM1x1 = Parameter(name = 'CKM1x1',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM1x1}')

CKM1x2 = Parameter(name = 'CKM1x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.sin(cabi)',
                   texname = '\\text{CKM1x2}')

CKM1x3 = Parameter(name = 'CKM1x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM1x3}')

CKM2x1 = Parameter(name = 'CKM2x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '-cmath.sin(cabi)',
                   texname = '\\text{CKM2x1}')

CKM2x2 = Parameter(name = 'CKM2x2',
                   nature = 'internal',
                   type = 'complex',
                   value = 'cmath.cos(cabi)',
                   texname = '\\text{CKM2x2}')

CKM2x3 = Parameter(name = 'CKM2x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM2x3}')

CKM3x1 = Parameter(name = 'CKM3x1',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x1}')

CKM3x2 = Parameter(name = 'CKM3x2',
                   nature = 'internal',
                   type = 'complex',
                   value = '0',
                   texname = '\\text{CKM3x2}')

CKM3x3 = Parameter(name = 'CKM3x3',
                   nature = 'internal',
                   type = 'complex',
                   value = '1',
                   texname = '\\text{CKM3x3}')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yc = Parameter(name = 'yc',
               nature = 'internal',
               type = 'real',
               value = '(ymc*cmath.sqrt(2))/vev',
               texname = '\\text{yc}')

ydo = Parameter(name = 'ydo',
                nature = 'internal',
                type = 'real',
                value = '(ymdo*cmath.sqrt(2))/vev',
                texname = '\\text{ydo}')

ye = Parameter(name = 'ye',
               nature = 'internal',
               type = 'real',
               value = '(yme*cmath.sqrt(2))/vev',
               texname = '\\text{ye}')

ym = Parameter(name = 'ym',
               nature = 'internal',
               type = 'real',
               value = '(ymm*cmath.sqrt(2))/vev',
               texname = '\\text{ym}')

ys = Parameter(name = 'ys',
               nature = 'internal',
               type = 'real',
               value = '(yms*cmath.sqrt(2))/vev',
               texname = '\\text{ys}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

yup = Parameter(name = 'yup',
                nature = 'internal',
                type = 'real',
                value = '(ymup*cmath.sqrt(2))/vev',
                texname = '\\text{yup}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

