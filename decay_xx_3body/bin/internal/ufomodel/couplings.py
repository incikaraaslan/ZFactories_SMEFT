# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 14.1.0 for Microsoft Windows (64-bit) (July 16, 2024)
# Date: Thu 9 Jul 2026 16:42:24


from object_library import all_couplings, Coupling

from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot



GC_1 = Coupling(name = 'GC_1',
                value = '-0.3333333333333333*(ee*complex(0,1))',
                order = {'QED':1})

GC_2 = Coupling(name = 'GC_2',
                value = '(2*ee*complex(0,1))/3.',
                order = {'QED':1})

GC_3 = Coupling(name = 'GC_3',
                value = '-(ee*complex(0,1))',
                order = {'QED':1})

GC_4 = Coupling(name = 'GC_4',
                value = 'ee*complex(0,1)',
                order = {'QED':1})

GC_5 = Coupling(name = 'GC_5',
                value = 'ee**2*complex(0,1)',
                order = {'QED':2})

GC_6 = Coupling(name = 'GC_6',
                value = '-G',
                order = {'QCD':1})

GC_7 = Coupling(name = 'GC_7',
                value = 'complex(0,1)*G',
                order = {'QCD':1})

GC_8 = Coupling(name = 'GC_8',
                value = 'complex(0,1)*G**2',
                order = {'QCD':2})

GC_9 = Coupling(name = 'GC_9',
                value = '-6*complex(0,1)*lam',
                order = {'QED':2})

GC_10 = Coupling(name = 'GC_10',
                 value = '-((CDHidQX*CKM1x1)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM1x1*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_11 = Coupling(name = 'GC_11',
                 value = '-0.5*(CDHidsQXI*CKM1x1)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM1x1*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_12 = Coupling(name = 'GC_12',
                 value = '-((CDHidQX*CKM1x2)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM1x2*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_13 = Coupling(name = 'GC_13',
                 value = '-0.5*(CDHidsQXI*CKM1x2)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM1x2*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_14 = Coupling(name = 'GC_14',
                 value = '-((CDHidQX*CKM1x3)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM1x3*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_15 = Coupling(name = 'GC_15',
                 value = '-0.5*(CDHidsQXI*CKM1x3)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM1x3*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_16 = Coupling(name = 'GC_16',
                 value = '-((CDHidQX*CKM2x1)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM2x1*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_17 = Coupling(name = 'GC_17',
                 value = '-0.5*(CDHidsQXI*CKM2x1)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM2x1*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_18 = Coupling(name = 'GC_18',
                 value = '-((CDHidQX*CKM2x2)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM2x2*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_19 = Coupling(name = 'GC_19',
                 value = '-0.5*(CDHidsQXI*CKM2x2)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM2x2*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_20 = Coupling(name = 'GC_20',
                 value = '-((CDHidQX*CKM2x3)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM2x3*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_21 = Coupling(name = 'GC_21',
                 value = '-0.5*(CDHidsQXI*CKM2x3)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM2x3*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_22 = Coupling(name = 'GC_22',
                 value = '-((CDHidQX*CKM3x1)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM3x1*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_23 = Coupling(name = 'GC_23',
                 value = '-0.5*(CDHidsQXI*CKM3x1)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM3x1*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_24 = Coupling(name = 'GC_24',
                 value = '-((CDHidQX*CKM3x2)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM3x2*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_25 = Coupling(name = 'GC_25',
                 value = '-0.5*(CDHidsQXI*CKM3x2)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM3x2*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_26 = Coupling(name = 'GC_26',
                 value = '-((CDHidQX*CKM3x3)/(LamX**2*cmath.sqrt(2))) - (CDHidQXI*CKM3x3*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_27 = Coupling(name = 'GC_27',
                 value = '-0.5*(CDHidsQXI*CKM3x3)/(LamX**2*cmath.sqrt(2)) + (CDHidsQX*CKM3x3*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_28 = Coupling(name = 'GC_28',
                 value = '(-2*CXH3)/LamX**2 - (2*CXH4)/LamX**2',
                 order = {'VBEFT':1})

GC_29 = Coupling(name = 'GC_29',
                 value = '-(CDHieLX/(LamX**2*cmath.sqrt(2)))',
                 order = {'VBEFT':1})

GC_30 = Coupling(name = 'GC_30',
                 value = '-((CDHieLXI*complex(0,1))/(LamX**2*cmath.sqrt(2)))',
                 order = {'VBEFT':1})

GC_31 = Coupling(name = 'GC_31',
                 value = '(CDHiesLX*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_32 = Coupling(name = 'GC_32',
                 value = '-0.5*CDHiesLXI/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_33 = Coupling(name = 'GC_33',
                 value = '(CDHiQsuX*complex(0,1))/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_34 = Coupling(name = 'GC_34',
                 value = 'CDHiQsuXI/(2.*LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_35 = Coupling(name = 'GC_35',
                 value = '-(CDHiQuX/(LamX**2*cmath.sqrt(2)))',
                 order = {'VBEFT':1})

GC_36 = Coupling(name = 'GC_36',
                 value = '(CDHiQuXI*complex(0,1))/(LamX**2*cmath.sqrt(2))',
                 order = {'VBEFT':1})

GC_37 = Coupling(name = 'GC_37',
                 value = '(8*cw**2*CXB2*complex(0,1))/LamX**2',
                 order = {'VBEFT':1})

GC_38 = Coupling(name = 'GC_38',
                 value = '(4*cw*CXB3*complex(0,1))/LamX**2',
                 order = {'VBEFT':1})

GC_39 = Coupling(name = 'GC_39',
                 value = '(cw*CXd)/LamX**2',
                 order = {'VBEFT':1})

GC_40 = Coupling(name = 'GC_40',
                 value = '(cw*CXe)/LamX**2',
                 order = {'VBEFT':1})

GC_41 = Coupling(name = 'GC_41',
                 value = '-(CXfd/LamX**2)',
                 order = {'VBEFT':1})

GC_42 = Coupling(name = 'GC_42',
                 value = '-((CXfdI*complex(0,1))/LamX**2)',
                 order = {'VBEFT':1})

GC_43 = Coupling(name = 'GC_43',
                 value = '-(CXfL/LamX**2)',
                 order = {'VBEFT':1})

GC_44 = Coupling(name = 'GC_44',
                 value = '-((CXfLI*complex(0,1))/LamX**2)',
                 order = {'VBEFT':1})

GC_45 = Coupling(name = 'GC_45',
                 value = '-(CXfQ/LamX**2)',
                 order = {'VBEFT':1})

GC_46 = Coupling(name = 'GC_46',
                 value = '-((CXfQI*complex(0,1))/LamX**2)',
                 order = {'VBEFT':1})

GC_47 = Coupling(name = 'GC_47',
                 value = '-(CXfu/LamX**2)',
                 order = {'VBEFT':1})

GC_48 = Coupling(name = 'GC_48',
                 value = '-((CXfuI*complex(0,1))/LamX**2)',
                 order = {'VBEFT':1})

GC_49 = Coupling(name = 'GC_49',
                 value = '(cw*CXHiB*complex(0,1))/LamX**2',
                 order = {'VBEFT':1})

GC_50 = Coupling(name = 'GC_50',
                 value = '(CXHiX*complex(0,1))/LamX**2',
                 order = {'VBEFT':1})

GC_51 = Coupling(name = 'GC_51',
                 value = '(cw*CXl)/LamX**2',
                 order = {'VBEFT':1})

GC_52 = Coupling(name = 'GC_52',
                 value = '(cw*CXq)/LamX**2',
                 order = {'VBEFT':1})

GC_53 = Coupling(name = 'GC_53',
                 value = '(cw*CXu)/LamX**2',
                 order = {'VBEFT':1})

GC_54 = Coupling(name = 'GC_54',
                 value = '(-2*CXW2*complex(0,1))/LamX**2',
                 order = {'VBEFT':1})

GC_55 = Coupling(name = 'GC_55',
                 value = '(2*cw**2*CXW2*complex(0,1))/LamX**2',
                 order = {'VBEFT':1})

GC_56 = Coupling(name = 'GC_56',
                 value = '(-2*CXfdI*ee*complex(0,1))/(3.*LamX**2)',
                 order = {'QED':1,'VBEFT':1})

GC_57 = Coupling(name = 'GC_57',
                 value = '(-2*CXfLI*ee*complex(0,1))/LamX**2',
                 order = {'QED':1,'VBEFT':1})

GC_58 = Coupling(name = 'GC_58',
                 value = '(-2*CXfQI*ee*complex(0,1))/(3.*LamX**2)',
                 order = {'QED':1,'VBEFT':1})

GC_59 = Coupling(name = 'GC_59',
                 value = '(4*CXfQI*ee*complex(0,1))/(3.*LamX**2)',
                 order = {'QED':1,'VBEFT':1})

GC_60 = Coupling(name = 'GC_60',
                 value = '(4*CXfuI*ee*complex(0,1))/(3.*LamX**2)',
                 order = {'QED':1,'VBEFT':1})

GC_61 = Coupling(name = 'GC_61',
                 value = '(-2*CXW2*ee*complex(0,1))/LamX**2',
                 order = {'QED':1,'VBEFT':1})

GC_62 = Coupling(name = 'GC_62',
                 value = '(4*CXW2*ee**2*complex(0,1))/LamX**2',
                 order = {'QED':2,'VBEFT':1})

GC_63 = Coupling(name = 'GC_63',
                 value = '(2*CXfdI*complex(0,1)*G)/LamX**2',
                 order = {'QCD':1,'VBEFT':1})

GC_64 = Coupling(name = 'GC_64',
                 value = '(2*CXfQI*complex(0,1)*G)/LamX**2',
                 order = {'QCD':1,'VBEFT':1})

GC_65 = Coupling(name = 'GC_65',
                 value = '(2*CXfuI*complex(0,1)*G)/LamX**2',
                 order = {'QCD':1,'VBEFT':1})

GC_66 = Coupling(name = 'GC_66',
                 value = '-0.5*(CDHidQX*ee)/(LamX**2*sw) - (CDHidQXI*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_67 = Coupling(name = 'GC_67',
                 value = '(CDHidQX*ee)/(2.*LamX**2*sw) - (CDHidQXI*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_68 = Coupling(name = 'GC_68',
                 value = '(CDHidsQXI*ee)/(4.*LamX**2*sw) - (CDHidsQX*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_69 = Coupling(name = 'GC_69',
                 value = '(CDHidsQXI*ee)/(4.*LamX**2*sw) + (CDHidsQX*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_70 = Coupling(name = 'GC_70',
                 value = '-0.5*(CDHieLX*ee)/(LamX**2*sw) - (CDHieLXI*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_71 = Coupling(name = 'GC_71',
                 value = '(CDHieLX*ee)/(2.*LamX**2*sw) - (CDHieLXI*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_72 = Coupling(name = 'GC_72',
                 value = '(CDHiesLXI*ee)/(4.*LamX**2*sw) - (CDHiesLX*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_73 = Coupling(name = 'GC_73',
                 value = '(CDHiesLXI*ee)/(4.*LamX**2*sw) + (CDHiesLX*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_74 = Coupling(name = 'GC_74',
                 value = '-0.25*(CDHiQsuXI*CKM1x1*ee)/(LamX**2*sw) - (CDHiQsuX*CKM1x1*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_75 = Coupling(name = 'GC_75',
                 value = '-0.5*(CDHiQuX*CKM1x1*ee)/(LamX**2*sw) + (CDHiQuXI*CKM1x1*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_76 = Coupling(name = 'GC_76',
                 value = '-0.25*(CDHiQsuXI*CKM1x2*ee)/(LamX**2*sw) - (CDHiQsuX*CKM1x2*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_77 = Coupling(name = 'GC_77',
                 value = '-0.5*(CDHiQuX*CKM1x2*ee)/(LamX**2*sw) + (CDHiQuXI*CKM1x2*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_78 = Coupling(name = 'GC_78',
                 value = '-0.25*(CDHiQsuXI*CKM1x3*ee)/(LamX**2*sw) - (CDHiQsuX*CKM1x3*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_79 = Coupling(name = 'GC_79',
                 value = '-0.5*(CDHiQuX*CKM1x3*ee)/(LamX**2*sw) + (CDHiQuXI*CKM1x3*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_80 = Coupling(name = 'GC_80',
                 value = '-0.25*(CDHiQsuXI*CKM2x1*ee)/(LamX**2*sw) - (CDHiQsuX*CKM2x1*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_81 = Coupling(name = 'GC_81',
                 value = '-0.5*(CDHiQuX*CKM2x1*ee)/(LamX**2*sw) + (CDHiQuXI*CKM2x1*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_82 = Coupling(name = 'GC_82',
                 value = '-0.25*(CDHiQsuXI*CKM2x2*ee)/(LamX**2*sw) - (CDHiQsuX*CKM2x2*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_83 = Coupling(name = 'GC_83',
                 value = '-0.5*(CDHiQuX*CKM2x2*ee)/(LamX**2*sw) + (CDHiQuXI*CKM2x2*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_84 = Coupling(name = 'GC_84',
                 value = '-0.25*(CDHiQsuXI*CKM2x3*ee)/(LamX**2*sw) - (CDHiQsuX*CKM2x3*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_85 = Coupling(name = 'GC_85',
                 value = '-0.5*(CDHiQuX*CKM2x3*ee)/(LamX**2*sw) + (CDHiQuXI*CKM2x3*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_86 = Coupling(name = 'GC_86',
                 value = '-0.25*(CDHiQsuXI*CKM3x1*ee)/(LamX**2*sw) - (CDHiQsuX*CKM3x1*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_87 = Coupling(name = 'GC_87',
                 value = '-0.5*(CDHiQuX*CKM3x1*ee)/(LamX**2*sw) + (CDHiQuXI*CKM3x1*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_88 = Coupling(name = 'GC_88',
                 value = '-0.25*(CDHiQsuXI*CKM3x2*ee)/(LamX**2*sw) - (CDHiQsuX*CKM3x2*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_89 = Coupling(name = 'GC_89',
                 value = '-0.5*(CDHiQuX*CKM3x2*ee)/(LamX**2*sw) + (CDHiQuXI*CKM3x2*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_90 = Coupling(name = 'GC_90',
                 value = '-0.25*(CDHiQsuXI*CKM3x3*ee)/(LamX**2*sw) - (CDHiQsuX*CKM3x3*ee*complex(0,1))/(4.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_91 = Coupling(name = 'GC_91',
                 value = '-0.5*(CDHiQuX*CKM3x3*ee)/(LamX**2*sw) + (CDHiQuXI*CKM3x3*ee*complex(0,1))/(2.*LamX**2*sw)',
                 order = {'QED':1,'VBEFT':1})

GC_92 = Coupling(name = 'GC_92',
                 value = '(ee**2*complex(0,1))/(2.*sw**2)',
                 order = {'QED':2})

GC_93 = Coupling(name = 'GC_93',
                 value = '-((ee**2*complex(0,1))/sw**2)',
                 order = {'QED':2})

GC_94 = Coupling(name = 'GC_94',
                 value = '(cw**2*ee**2*complex(0,1))/sw**2',
                 order = {'QED':2})

GC_95 = Coupling(name = 'GC_95',
                 value = '(-4*CXW2*ee**2*complex(0,1))/(LamX**2*sw**2)',
                 order = {'QED':2,'VBEFT':1})

GC_96 = Coupling(name = 'GC_96',
                 value = '(-2*cw**2*CXW2*ee**2*complex(0,1))/(LamX**2*sw**2)',
                 order = {'QED':2,'VBEFT':1})

GC_97 = Coupling(name = 'GC_97',
                 value = '(ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_98 = Coupling(name = 'GC_98',
                 value = '(CKM1x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_99 = Coupling(name = 'GC_99',
                 value = '(CKM1x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                 order = {'QED':1})

GC_100 = Coupling(name = 'GC_100',
                  value = '(CKM1x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_101 = Coupling(name = 'GC_101',
                  value = '(CKM2x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_102 = Coupling(name = 'GC_102',
                  value = '(CKM2x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_103 = Coupling(name = 'GC_103',
                  value = '(CKM2x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_104 = Coupling(name = 'GC_104',
                  value = '(CKM3x1*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_105 = Coupling(name = 'GC_105',
                  value = '(CKM3x2*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_106 = Coupling(name = 'GC_106',
                  value = '(CKM3x3*ee*complex(0,1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_107 = Coupling(name = 'GC_107',
                  value = '-0.5*(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_108 = Coupling(name = 'GC_108',
                  value = '(cw*ee*complex(0,1))/(2.*sw)',
                  order = {'QED':1})

GC_109 = Coupling(name = 'GC_109',
                  value = '(cw*ee*complex(0,1))/sw',
                  order = {'QED':1})

GC_110 = Coupling(name = 'GC_110',
                  value = '(-2*cw*ee**2*complex(0,1))/sw',
                  order = {'QED':2})

GC_111 = Coupling(name = 'GC_111',
                  value = '-0.25*(CDHiesLX*ee*complex(0,1))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_112 = Coupling(name = 'GC_112',
                  value = '(CDHiesLXI*ee)/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_113 = Coupling(name = 'GC_113',
                  value = '(CDHiQsuX*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_114 = Coupling(name = 'GC_114',
                  value = '(CXfLI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_115 = Coupling(name = 'GC_115',
                  value = '(CKM1x1*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_116 = Coupling(name = 'GC_116',
                  value = '(CKM1x2*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_117 = Coupling(name = 'GC_117',
                  value = '(CKM1x3*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_118 = Coupling(name = 'GC_118',
                  value = '(CKM2x1*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_119 = Coupling(name = 'GC_119',
                  value = '(CKM2x2*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_120 = Coupling(name = 'GC_120',
                  value = '(CKM2x3*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_121 = Coupling(name = 'GC_121',
                  value = '(CKM3x1*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_122 = Coupling(name = 'GC_122',
                  value = '(CKM3x2*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_123 = Coupling(name = 'GC_123',
                  value = '(CKM3x3*CXfQI*ee*complex(0,1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_124 = Coupling(name = 'GC_124',
                  value = '(-2*cw*CXW2*ee*complex(0,1))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_125 = Coupling(name = 'GC_125',
                  value = '(4*cw*CXW2*ee**2*complex(0,1))/(LamX**2*sw)',
                  order = {'QED':2,'VBEFT':1})

GC_126 = Coupling(name = 'GC_126',
                  value = '-0.16666666666666666*(ee*complex(0,1)*sw)/cw',
                  order = {'QED':1})

GC_127 = Coupling(name = 'GC_127',
                  value = '(ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_128 = Coupling(name = 'GC_128',
                  value = '(-8*cw*CXB2*complex(0,1)*sw)/LamX**2',
                  order = {'VBEFT':1})

GC_129 = Coupling(name = 'GC_129',
                  value = '(-4*CXB3*complex(0,1)*sw)/LamX**2',
                  order = {'VBEFT':1})

GC_130 = Coupling(name = 'GC_130',
                  value = '-((CXd*sw)/LamX**2)',
                  order = {'VBEFT':1})

GC_131 = Coupling(name = 'GC_131',
                  value = '-((CXe*sw)/LamX**2)',
                  order = {'VBEFT':1})

GC_132 = Coupling(name = 'GC_132',
                  value = '-((CXHiB*complex(0,1)*sw)/LamX**2)',
                  order = {'VBEFT':1})

GC_133 = Coupling(name = 'GC_133',
                  value = '-((CXl*sw)/LamX**2)',
                  order = {'VBEFT':1})

GC_134 = Coupling(name = 'GC_134',
                  value = '-((CXq*sw)/LamX**2)',
                  order = {'VBEFT':1})

GC_135 = Coupling(name = 'GC_135',
                  value = '-((CXu*sw)/LamX**2)',
                  order = {'VBEFT':1})

GC_136 = Coupling(name = 'GC_136',
                  value = '(2*cw*CXW2*complex(0,1)*sw)/LamX**2',
                  order = {'VBEFT':1})

GC_137 = Coupling(name = 'GC_137',
                  value = '(CDHiQsuX*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_138 = Coupling(name = 'GC_138',
                  value = '(2*CXfdI*ee*complex(0,1)*sw)/(3.*cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_139 = Coupling(name = 'GC_139',
                  value = '(-4*CXfuI*ee*complex(0,1)*sw)/(3.*cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_140 = Coupling(name = 'GC_140',
                  value = '(8*CXB2*complex(0,1)*sw**2)/LamX**2',
                  order = {'VBEFT':1})

GC_141 = Coupling(name = 'GC_141',
                  value = '(-2*CXW2*complex(0,1)*sw**2)/LamX**2',
                  order = {'VBEFT':1})

GC_142 = Coupling(name = 'GC_142',
                  value = '(cw*ee*complex(0,1))/(2.*sw) + (ee*complex(0,1)*sw)/(2.*cw)',
                  order = {'QED':1})

GC_143 = Coupling(name = 'GC_143',
                  value = '(CDHieLX*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHieLX*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_144 = Coupling(name = 'GC_144',
                  value = '(CDHieLXI*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHieLXI*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_145 = Coupling(name = 'GC_145',
                  value = '-0.25*(CDHiesLX*cw*ee*complex(0,1))/(LamX**2*sw*cmath.sqrt(2)) - (CDHiesLX*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_146 = Coupling(name = 'GC_146',
                  value = '(CDHiesLXI*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHiesLXI*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_147 = Coupling(name = 'GC_147',
                  value = '(CDHiQsuX*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHiQsuX*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_148 = Coupling(name = 'GC_148',
                  value = '(CDHiQsuXI*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHiQsuXI*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_149 = Coupling(name = 'GC_149',
                  value = '-0.5*(CDHiQuX*cw*ee)/(LamX**2*sw*cmath.sqrt(2)) - (CDHiQuX*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_150 = Coupling(name = 'GC_150',
                  value = '(CDHiQuXI*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHiQuXI*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_151 = Coupling(name = 'GC_151',
                  value = '(CDHidQX*CKM1x1*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM1x1*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM1x1*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM1x1*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_152 = Coupling(name = 'GC_152',
                  value = '(CDHidsQXI*CKM1x1*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM1x1*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM1x1*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM1x1*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_153 = Coupling(name = 'GC_153',
                  value = '(CDHidQX*CKM1x2*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM1x2*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM1x2*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM1x2*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_154 = Coupling(name = 'GC_154',
                  value = '(CDHidsQXI*CKM1x2*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM1x2*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM1x2*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM1x2*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_155 = Coupling(name = 'GC_155',
                  value = '(CDHidQX*CKM1x3*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM1x3*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM1x3*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM1x3*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_156 = Coupling(name = 'GC_156',
                  value = '(CDHidsQXI*CKM1x3*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM1x3*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM1x3*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM1x3*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_157 = Coupling(name = 'GC_157',
                  value = '(CDHidQX*CKM2x1*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM2x1*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM2x1*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM2x1*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_158 = Coupling(name = 'GC_158',
                  value = '(CDHidsQXI*CKM2x1*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM2x1*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM2x1*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM2x1*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_159 = Coupling(name = 'GC_159',
                  value = '(CDHidQX*CKM2x2*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM2x2*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM2x2*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM2x2*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_160 = Coupling(name = 'GC_160',
                  value = '(CDHidsQXI*CKM2x2*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM2x2*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM2x2*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM2x2*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_161 = Coupling(name = 'GC_161',
                  value = '(CDHidQX*CKM2x3*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM2x3*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM2x3*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM2x3*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_162 = Coupling(name = 'GC_162',
                  value = '(CDHidsQXI*CKM2x3*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM2x3*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM2x3*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM2x3*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_163 = Coupling(name = 'GC_163',
                  value = '(CDHidQX*CKM3x1*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM3x1*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM3x1*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM3x1*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_164 = Coupling(name = 'GC_164',
                  value = '(CDHidsQXI*CKM3x1*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM3x1*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM3x1*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM3x1*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_165 = Coupling(name = 'GC_165',
                  value = '(CDHidQX*CKM3x2*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM3x2*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM3x2*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM3x2*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_166 = Coupling(name = 'GC_166',
                  value = '(CDHidsQXI*CKM3x2*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM3x2*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM3x2*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM3x2*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_167 = Coupling(name = 'GC_167',
                  value = '(CDHidQX*CKM3x3*cw*ee)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM3x3*cw*ee*complex(0,1))/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM3x3*ee*sw)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM3x3*ee*complex(0,1)*sw)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_168 = Coupling(name = 'GC_168',
                  value = '(CDHidsQXI*CKM3x3*cw*ee)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM3x3*cw*ee*complex(0,1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM3x3*ee*sw)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM3x3*ee*complex(0,1)*sw)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_169 = Coupling(name = 'GC_169',
                  value = '-((cw*CXfLI*ee*complex(0,1))/(LamX**2*sw)) + (CXfLI*ee*complex(0,1)*sw)/(cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_170 = Coupling(name = 'GC_170',
                  value = '(cw*CXfLI*ee*complex(0,1))/(LamX**2*sw) + (CXfLI*ee*complex(0,1)*sw)/(cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_171 = Coupling(name = 'GC_171',
                  value = '-((cw*CXfQI*ee*complex(0,1))/(LamX**2*sw)) - (CXfQI*ee*complex(0,1)*sw)/(3.*cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_172 = Coupling(name = 'GC_172',
                  value = '(cw*CXfQI*ee*complex(0,1))/(LamX**2*sw) - (CXfQI*ee*complex(0,1)*sw)/(3.*cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_173 = Coupling(name = 'GC_173',
                  value = '(-2*cw*CXH3I*ee*complex(0,1))/(LamX**2*sw) + (2*cw*CXH4I*ee*complex(0,1))/(LamX**2*sw) - (2*CXH3I*ee*complex(0,1)*sw)/(cw*LamX**2) + (2*CXH4I*ee*complex(0,1)*sw)/(cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_174 = Coupling(name = 'GC_174',
                  value = '-((cw**2*CXHiBI*ee)/(LamX**2*sw)) - (CXHiBI*ee*sw)/LamX**2',
                  order = {'QED':1,'VBEFT':1})

GC_175 = Coupling(name = 'GC_175',
                  value = '-((cw*CXHiXI*ee)/(LamX**2*sw)) - (CXHiXI*ee*sw)/(cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_176 = Coupling(name = 'GC_176',
                  value = 'ee**2*complex(0,1) + (cw**2*ee**2*complex(0,1))/(2.*sw**2) + (ee**2*complex(0,1)*sw**2)/(2.*cw**2)',
                  order = {'QED':2})

GC_177 = Coupling(name = 'GC_177',
                  value = '(cw*CXHiBI*ee)/LamX**2 + (CXHiBI*ee*sw**2)/(cw*LamX**2)',
                  order = {'QED':1,'VBEFT':1})

GC_178 = Coupling(name = 'GC_178',
                  value = '-6*complex(0,1)*lam*vev',
                  order = {'QED':1})

GC_179 = Coupling(name = 'GC_179',
                  value = '(cw*CXHiB*complex(0,1)*vev)/LamX**2',
                  order = {'QED':-1,'VBEFT':1})

GC_180 = Coupling(name = 'GC_180',
                  value = '(CXHiX*complex(0,1)*vev)/LamX**2',
                  order = {'QED':-1,'VBEFT':1})

GC_181 = Coupling(name = 'GC_181',
                  value = '(ee**2*complex(0,1)*vev)/(2.*sw**2)',
                  order = {'QED':1})

GC_182 = Coupling(name = 'GC_182',
                  value = '-0.25*(CDHidsQX*ee*complex(0,1)*vev)/(LamX**2*sw)',
                  order = {'VBEFT':1})

GC_183 = Coupling(name = 'GC_183',
                  value = '-0.25*(CDHidsQXI*ee*vev)/(LamX**2*sw)',
                  order = {'VBEFT':1})

GC_184 = Coupling(name = 'GC_184',
                  value = '-((CXHiB*complex(0,1)*sw*vev)/LamX**2)',
                  order = {'QED':-1,'VBEFT':1})

GC_185 = Coupling(name = 'GC_185',
                  value = '-0.25*(CDHidsQX*CKM2x3*ee*complex(0,1)*sw*vev)/(cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_186 = Coupling(name = 'GC_186',
                  value = '-0.25*(CDHidsQXI*CKM2x3*ee*sw*vev)/(cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_187 = Coupling(name = 'GC_187',
                  value = '(-2*CXH3*vev)/LamX**2 - (2*CXH4*vev)/LamX**2',
                  order = {'QED':-1,'VBEFT':1})

GC_188 = Coupling(name = 'GC_188',
                  value = '-0.5*(CDHidQX*ee*vev)/(LamX**2*sw) - (CDHidQXI*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_189 = Coupling(name = 'GC_189',
                  value = '(CDHidQX*ee*vev)/(2.*LamX**2*sw) - (CDHidQXI*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_190 = Coupling(name = 'GC_190',
                  value = '(CDHidsQXI*ee*vev)/(4.*LamX**2*sw) - (CDHidsQX*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_191 = Coupling(name = 'GC_191',
                  value = '(CDHidsQXI*ee*vev)/(4.*LamX**2*sw) + (CDHidsQX*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_192 = Coupling(name = 'GC_192',
                  value = '-0.5*(CDHieLX*ee*vev)/(LamX**2*sw) - (CDHieLXI*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_193 = Coupling(name = 'GC_193',
                  value = '(CDHieLX*ee*vev)/(2.*LamX**2*sw) - (CDHieLXI*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_194 = Coupling(name = 'GC_194',
                  value = '(CDHiesLXI*ee*vev)/(4.*LamX**2*sw) - (CDHiesLX*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_195 = Coupling(name = 'GC_195',
                  value = '(CDHiesLXI*ee*vev)/(4.*LamX**2*sw) + (CDHiesLX*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_196 = Coupling(name = 'GC_196',
                  value = '-0.25*(CDHiQsuXI*CKM1x1*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM1x1*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_197 = Coupling(name = 'GC_197',
                  value = '-0.5*(CDHiQuX*CKM1x1*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM1x1*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_198 = Coupling(name = 'GC_198',
                  value = '-0.25*(CDHiQsuXI*CKM1x2*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM1x2*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_199 = Coupling(name = 'GC_199',
                  value = '-0.5*(CDHiQuX*CKM1x2*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM1x2*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_200 = Coupling(name = 'GC_200',
                  value = '-0.25*(CDHiQsuXI*CKM1x3*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM1x3*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_201 = Coupling(name = 'GC_201',
                  value = '-0.5*(CDHiQuX*CKM1x3*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM1x3*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_202 = Coupling(name = 'GC_202',
                  value = '-0.25*(CDHiQsuXI*CKM2x1*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM2x1*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_203 = Coupling(name = 'GC_203',
                  value = '-0.5*(CDHiQuX*CKM2x1*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM2x1*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_204 = Coupling(name = 'GC_204',
                  value = '-0.25*(CDHiQsuXI*CKM2x2*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM2x2*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_205 = Coupling(name = 'GC_205',
                  value = '-0.5*(CDHiQuX*CKM2x2*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM2x2*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_206 = Coupling(name = 'GC_206',
                  value = '-0.25*(CDHiQsuXI*CKM2x3*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM2x3*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_207 = Coupling(name = 'GC_207',
                  value = '-0.5*(CDHiQuX*CKM2x3*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM2x3*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_208 = Coupling(name = 'GC_208',
                  value = '-0.25*(CDHiQsuXI*CKM3x1*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM3x1*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_209 = Coupling(name = 'GC_209',
                  value = '-0.5*(CDHiQuX*CKM3x1*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM3x1*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_210 = Coupling(name = 'GC_210',
                  value = '-0.25*(CDHiQsuXI*CKM3x2*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM3x2*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_211 = Coupling(name = 'GC_211',
                  value = '-0.5*(CDHiQuX*CKM3x2*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM3x2*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_212 = Coupling(name = 'GC_212',
                  value = '-0.25*(CDHiQsuXI*CKM3x3*ee*vev)/(LamX**2*sw) - (CDHiQsuX*CKM3x3*ee*complex(0,1)*vev)/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_213 = Coupling(name = 'GC_213',
                  value = '-0.5*(CDHiQuX*CKM3x3*ee*vev)/(LamX**2*sw) + (CDHiQuXI*CKM3x3*ee*complex(0,1)*vev)/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_214 = Coupling(name = 'GC_214',
                  value = '(CDHidsQXI*CKM2x3*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM2x3*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_215 = Coupling(name = 'GC_215',
                  value = '(CDHieLX*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHieLX*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_216 = Coupling(name = 'GC_216',
                  value = '(CDHieLXI*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHieLXI*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_217 = Coupling(name = 'GC_217',
                  value = '-0.25*(CDHiesLX*cw*ee*complex(0,1)*vev)/(LamX**2*sw*cmath.sqrt(2)) - (CDHiesLX*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_218 = Coupling(name = 'GC_218',
                  value = '(CDHiesLXI*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHiesLXI*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_219 = Coupling(name = 'GC_219',
                  value = '(CDHiQsuX*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHiQsuX*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_220 = Coupling(name = 'GC_220',
                  value = '(CDHiQsuXI*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHiQsuXI*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_221 = Coupling(name = 'GC_221',
                  value = '-0.5*(CDHiQuX*cw*ee*vev)/(LamX**2*sw*cmath.sqrt(2)) - (CDHiQuX*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_222 = Coupling(name = 'GC_222',
                  value = '(CDHiQuXI*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHiQuXI*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_223 = Coupling(name = 'GC_223',
                  value = '(CDHidQX*CKM1x1*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM1x1*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM1x1*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM1x1*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_224 = Coupling(name = 'GC_224',
                  value = '(CDHidsQXI*CKM1x1*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM1x1*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM1x1*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM1x1*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_225 = Coupling(name = 'GC_225',
                  value = '(CDHidQX*CKM1x2*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM1x2*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM1x2*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM1x2*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_226 = Coupling(name = 'GC_226',
                  value = '(CDHidsQXI*CKM1x2*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM1x2*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM1x2*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM1x2*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_227 = Coupling(name = 'GC_227',
                  value = '(CDHidQX*CKM1x3*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM1x3*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM1x3*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM1x3*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_228 = Coupling(name = 'GC_228',
                  value = '(CDHidsQXI*CKM1x3*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM1x3*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM1x3*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM1x3*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_229 = Coupling(name = 'GC_229',
                  value = '(CDHidQX*CKM2x1*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM2x1*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM2x1*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM2x1*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_230 = Coupling(name = 'GC_230',
                  value = '(CDHidsQXI*CKM2x1*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM2x1*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM2x1*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM2x1*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_231 = Coupling(name = 'GC_231',
                  value = '(CDHidQX*CKM2x2*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM2x2*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM2x2*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM2x2*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_232 = Coupling(name = 'GC_232',
                  value = '(CDHidsQXI*CKM2x2*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM2x2*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM2x2*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM2x2*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_233 = Coupling(name = 'GC_233',
                  value = '(CDHidQX*CKM2x3*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM2x3*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM2x3*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM2x3*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_234 = Coupling(name = 'GC_234',
                  value = '(CDHidQX*CKM3x1*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM3x1*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM3x1*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM3x1*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_235 = Coupling(name = 'GC_235',
                  value = '(CDHidsQXI*CKM3x1*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM3x1*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM3x1*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM3x1*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_236 = Coupling(name = 'GC_236',
                  value = '(CDHidQX*CKM3x2*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM3x2*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM3x2*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM3x2*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_237 = Coupling(name = 'GC_237',
                  value = '(CDHidsQXI*CKM3x2*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM3x2*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM3x2*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM3x2*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_238 = Coupling(name = 'GC_238',
                  value = '(CDHidQX*CKM3x3*cw*ee*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*CKM3x3*cw*ee*complex(0,1)*vev)/(2.*LamX**2*sw*cmath.sqrt(2)) + (CDHidQX*CKM3x3*ee*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*CKM3x3*ee*complex(0,1)*sw*vev)/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_239 = Coupling(name = 'GC_239',
                  value = '(CDHidsQXI*CKM3x3*cw*ee*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*CKM3x3*cw*ee*complex(0,1)*vev)/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*CKM3x3*ee*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*CKM3x3*ee*complex(0,1)*sw*vev)/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_240 = Coupling(name = 'GC_240',
                  value = '(-2*cw*CXH3I*ee*complex(0,1)*vev)/(LamX**2*sw) + (2*cw*CXH4I*ee*complex(0,1)*vev)/(LamX**2*sw) - (2*CXH3I*ee*complex(0,1)*sw*vev)/(cw*LamX**2) + (2*CXH4I*ee*complex(0,1)*sw*vev)/(cw*LamX**2)',
                  order = {'VBEFT':1})

GC_241 = Coupling(name = 'GC_241',
                  value = '-((cw**2*CXHiBI*ee*vev)/(LamX**2*sw)) - (CXHiBI*ee*sw*vev)/LamX**2',
                  order = {'VBEFT':1})

GC_242 = Coupling(name = 'GC_242',
                  value = '-((cw*CXHiXI*ee*vev)/(LamX**2*sw)) - (CXHiXI*ee*sw*vev)/(cw*LamX**2)',
                  order = {'VBEFT':1})

GC_243 = Coupling(name = 'GC_243',
                  value = 'ee**2*complex(0,1)*vev + (cw**2*ee**2*complex(0,1)*vev)/(2.*sw**2) + (ee**2*complex(0,1)*sw**2*vev)/(2.*cw**2)',
                  order = {'QED':1})

GC_244 = Coupling(name = 'GC_244',
                  value = '(cw*CXHiBI*ee*vev)/LamX**2 + (CXHiBI*ee*sw**2*vev)/(cw*LamX**2)',
                  order = {'VBEFT':1})

GC_245 = Coupling(name = 'GC_245',
                  value = '-((cw*CXH3I*ee*complex(0,1)*vev**2)/(LamX**2*sw)) + (cw*CXH4I*ee*complex(0,1)*vev**2)/(LamX**2*sw) - (CXH3I*ee*complex(0,1)*sw*vev**2)/(cw*LamX**2) + (CXH4I*ee*complex(0,1)*sw*vev**2)/(cw*LamX**2)',
                  order = {'QED':-1,'VBEFT':1})

GC_246 = Coupling(name = 'GC_246',
                  value = '-0.5*(cw**2*CXHiBI*ee*vev**2)/(LamX**2*sw) - (CXHiBI*ee*sw*vev**2)/(2.*LamX**2)',
                  order = {'QED':-1,'VBEFT':1})

GC_247 = Coupling(name = 'GC_247',
                  value = '-0.5*(cw*CXHiXI*ee*vev**2)/(LamX**2*sw) - (CXHiXI*ee*sw*vev**2)/(2.*cw*LamX**2)',
                  order = {'QED':-1,'VBEFT':1})

GC_248 = Coupling(name = 'GC_248',
                  value = '(cw*CXHiBI*ee*vev**2)/(2.*LamX**2) + (CXHiBI*ee*sw**2*vev**2)/(2.*cw*LamX**2)',
                  order = {'QED':-1,'VBEFT':1})

GC_249 = Coupling(name = 'GC_249',
                  value = '-((complex(0,1)*yb)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_250 = Coupling(name = 'GC_250',
                  value = '-((complex(0,1)*yc)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_251 = Coupling(name = 'GC_251',
                  value = '-((complex(0,1)*ydo)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_252 = Coupling(name = 'GC_252',
                  value = '-((complex(0,1)*ye)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_253 = Coupling(name = 'GC_253',
                  value = '-((complex(0,1)*ym)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_254 = Coupling(name = 'GC_254',
                  value = '-((complex(0,1)*ys)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_255 = Coupling(name = 'GC_255',
                  value = '-((complex(0,1)*yt)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_256 = Coupling(name = 'GC_256',
                  value = '-((complex(0,1)*ytau)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_257 = Coupling(name = 'GC_257',
                  value = '-((complex(0,1)*yup)/cmath.sqrt(2))',
                  order = {'QED':1})

GC_258 = Coupling(name = 'GC_258',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_259 = Coupling(name = 'GC_259',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM1x1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_260 = Coupling(name = 'GC_260',
                  value = '-((CDHidQX*complexconjugate(CKM1x1))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM1x1))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_261 = Coupling(name = 'GC_261',
                  value = '(CDHidsQXI*complexconjugate(CKM1x1))/(2.*LamX**2*cmath.sqrt(2)) + (CDHidsQX*complex(0,1)*complexconjugate(CKM1x1))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_262 = Coupling(name = 'GC_262',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM1x1))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM1x1))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_263 = Coupling(name = 'GC_263',
                  value = '(CDHiQuX*ee*complexconjugate(CKM1x1))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM1x1))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_264 = Coupling(name = 'GC_264',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM1x1))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM1x1))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM1x1))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM1x1))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_265 = Coupling(name = 'GC_265',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM1x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM1x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM1x1))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM1x1))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_266 = Coupling(name = 'GC_266',
                  value = '-0.25*(CDHiQsuXI*ee*vev*complexconjugate(CKM1x1))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM1x1))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_267 = Coupling(name = 'GC_267',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM1x1))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM1x1))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_268 = Coupling(name = 'GC_268',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM1x1))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM1x1))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM1x1))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM1x1))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_269 = Coupling(name = 'GC_269',
                  value = '(CDHidsQXI*cw*ee*vev*complexconjugate(CKM1x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM1x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*vev*complexconjugate(CKM1x1))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM1x1))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_270 = Coupling(name = 'GC_270',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_271 = Coupling(name = 'GC_271',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM1x2)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_272 = Coupling(name = 'GC_272',
                  value = '-((CDHidQX*complexconjugate(CKM1x2))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM1x2))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_273 = Coupling(name = 'GC_273',
                  value = '(CDHidsQXI*complexconjugate(CKM1x2))/(2.*LamX**2*cmath.sqrt(2)) + (CDHidsQX*complex(0,1)*complexconjugate(CKM1x2))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_274 = Coupling(name = 'GC_274',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM1x2))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM1x2))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_275 = Coupling(name = 'GC_275',
                  value = '(CDHiQuX*ee*complexconjugate(CKM1x2))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM1x2))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_276 = Coupling(name = 'GC_276',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM1x2))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM1x2))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM1x2))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM1x2))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_277 = Coupling(name = 'GC_277',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM1x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM1x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM1x2))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM1x2))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_278 = Coupling(name = 'GC_278',
                  value = '-0.25*(CDHiQsuXI*ee*vev*complexconjugate(CKM1x2))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM1x2))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_279 = Coupling(name = 'GC_279',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM1x2))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM1x2))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_280 = Coupling(name = 'GC_280',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM1x2))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM1x2))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM1x2))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM1x2))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_281 = Coupling(name = 'GC_281',
                  value = '(CDHidsQXI*cw*ee*vev*complexconjugate(CKM1x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM1x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*vev*complexconjugate(CKM1x2))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM1x2))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_282 = Coupling(name = 'GC_282',
                  value = '(ee*complex(0,1)*complexconjugate(CKM1x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_283 = Coupling(name = 'GC_283',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM1x3)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_284 = Coupling(name = 'GC_284',
                  value = '-((CDHidQX*complexconjugate(CKM1x3))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM1x3))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_285 = Coupling(name = 'GC_285',
                  value = '(CDHidsQXI*complexconjugate(CKM1x3))/(2.*LamX**2*cmath.sqrt(2)) + (CDHidsQX*complex(0,1)*complexconjugate(CKM1x3))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_286 = Coupling(name = 'GC_286',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM1x3))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM1x3))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_287 = Coupling(name = 'GC_287',
                  value = '(CDHiQuX*ee*complexconjugate(CKM1x3))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM1x3))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_288 = Coupling(name = 'GC_288',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM1x3))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM1x3))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM1x3))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM1x3))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_289 = Coupling(name = 'GC_289',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM1x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM1x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM1x3))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM1x3))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_290 = Coupling(name = 'GC_290',
                  value = '-0.25*(CDHiQsuXI*ee*vev*complexconjugate(CKM1x3))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM1x3))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_291 = Coupling(name = 'GC_291',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM1x3))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM1x3))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_292 = Coupling(name = 'GC_292',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM1x3))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM1x3))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM1x3))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM1x3))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_293 = Coupling(name = 'GC_293',
                  value = '(CDHidsQXI*cw*ee*vev*complexconjugate(CKM1x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM1x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*vev*complexconjugate(CKM1x3))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM1x3))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_294 = Coupling(name = 'GC_294',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_295 = Coupling(name = 'GC_295',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM2x1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_296 = Coupling(name = 'GC_296',
                  value = '-((CDHidQX*complexconjugate(CKM2x1))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM2x1))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_297 = Coupling(name = 'GC_297',
                  value = '(CDHidsQXI*complexconjugate(CKM2x1))/(2.*LamX**2*cmath.sqrt(2)) + (CDHidsQX*complex(0,1)*complexconjugate(CKM2x1))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_298 = Coupling(name = 'GC_298',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM2x1))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM2x1))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_299 = Coupling(name = 'GC_299',
                  value = '(CDHiQuX*ee*complexconjugate(CKM2x1))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM2x1))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_300 = Coupling(name = 'GC_300',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM2x1))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM2x1))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM2x1))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM2x1))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_301 = Coupling(name = 'GC_301',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM2x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM2x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM2x1))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM2x1))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_302 = Coupling(name = 'GC_302',
                  value = '-0.25*(CDHiQsuXI*ee*vev*complexconjugate(CKM2x1))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM2x1))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_303 = Coupling(name = 'GC_303',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM2x1))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM2x1))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_304 = Coupling(name = 'GC_304',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM2x1))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM2x1))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM2x1))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM2x1))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_305 = Coupling(name = 'GC_305',
                  value = '(CDHidsQXI*cw*ee*vev*complexconjugate(CKM2x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM2x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*vev*complexconjugate(CKM2x1))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM2x1))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_306 = Coupling(name = 'GC_306',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_307 = Coupling(name = 'GC_307',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM2x2)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_308 = Coupling(name = 'GC_308',
                  value = '-((CDHidQX*complexconjugate(CKM2x2))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM2x2))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_309 = Coupling(name = 'GC_309',
                  value = '(CDHidsQXI*complexconjugate(CKM2x2))/(2.*LamX**2*cmath.sqrt(2)) + (CDHidsQX*complex(0,1)*complexconjugate(CKM2x2))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_310 = Coupling(name = 'GC_310',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM2x2))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM2x2))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_311 = Coupling(name = 'GC_311',
                  value = '(CDHiQuX*ee*complexconjugate(CKM2x2))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM2x2))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_312 = Coupling(name = 'GC_312',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM2x2))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM2x2))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM2x2))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM2x2))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_313 = Coupling(name = 'GC_313',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM2x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM2x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM2x2))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM2x2))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_314 = Coupling(name = 'GC_314',
                  value = '-0.25*(CDHiQsuXI*ee*vev*complexconjugate(CKM2x2))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM2x2))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_315 = Coupling(name = 'GC_315',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM2x2))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM2x2))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_316 = Coupling(name = 'GC_316',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM2x2))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM2x2))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM2x2))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM2x2))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_317 = Coupling(name = 'GC_317',
                  value = '(CDHidsQXI*cw*ee*vev*complexconjugate(CKM2x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM2x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*vev*complexconjugate(CKM2x2))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM2x2))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_318 = Coupling(name = 'GC_318',
                  value = '(ee*complex(0,1)*complexconjugate(CKM2x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_319 = Coupling(name = 'GC_319',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM2x3)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_320 = Coupling(name = 'GC_320',
                  value = '-((CDHidQX*complexconjugate(CKM2x3))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM2x3))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_321 = Coupling(name = 'GC_321',
                  value = '(CDHidsQXI*complexconjugate(CKM2x3))/(2.*LamX**2*cmath.sqrt(2)) + (CDHidsQX*complex(0,1)*complexconjugate(CKM2x3))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_322 = Coupling(name = 'GC_322',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM2x3))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM2x3))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_323 = Coupling(name = 'GC_323',
                  value = '(CDHiQuX*ee*complexconjugate(CKM2x3))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM2x3))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_324 = Coupling(name = 'GC_324',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM2x3))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM2x3))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM2x3))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM2x3))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_325 = Coupling(name = 'GC_325',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM2x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM2x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM2x3))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM2x3))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_326 = Coupling(name = 'GC_326',
                  value = '-0.25*(CDHiQsuXI*ee*vev*complexconjugate(CKM2x3))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM2x3))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_327 = Coupling(name = 'GC_327',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM2x3))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM2x3))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_328 = Coupling(name = 'GC_328',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM2x3))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM2x3))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM2x3))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM2x3))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_329 = Coupling(name = 'GC_329',
                  value = '(CDHidsQXI*cw*ee*vev*complexconjugate(CKM2x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM2x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*vev*complexconjugate(CKM2x3))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM2x3))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_330 = Coupling(name = 'GC_330',
                  value = '(CDHidsQX*complex(0,1)*complexconjugate(CKM3x1))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_331 = Coupling(name = 'GC_331',
                  value = '(CDHidsQXI*complexconjugate(CKM3x1))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_332 = Coupling(name = 'GC_332',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x1))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_333 = Coupling(name = 'GC_333',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM3x1)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_334 = Coupling(name = 'GC_334',
                  value = '-((CDHidQX*complexconjugate(CKM3x1))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM3x1))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_335 = Coupling(name = 'GC_335',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM3x1))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM3x1))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_336 = Coupling(name = 'GC_336',
                  value = '(CDHiQuX*ee*complexconjugate(CKM3x1))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM3x1))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_337 = Coupling(name = 'GC_337',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM3x1))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM3x1))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM3x1))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM3x1))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_338 = Coupling(name = 'GC_338',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM3x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM3x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM3x1))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM3x1))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_339 = Coupling(name = 'GC_339',
                  value = '-0.25*(CDHiQsuXI*ee*vev*complexconjugate(CKM3x1))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM3x1))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_340 = Coupling(name = 'GC_340',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM3x1))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM3x1))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_341 = Coupling(name = 'GC_341',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM3x1))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM3x1))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM3x1))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM3x1))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_342 = Coupling(name = 'GC_342',
                  value = '(CDHidsQXI*cw*ee*vev*complexconjugate(CKM3x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM3x1))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*vev*complexconjugate(CKM3x1))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM3x1))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_343 = Coupling(name = 'GC_343',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x2))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_344 = Coupling(name = 'GC_344',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM3x2)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_345 = Coupling(name = 'GC_345',
                  value = '-((CDHidQX*complexconjugate(CKM3x2))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM3x2))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_346 = Coupling(name = 'GC_346',
                  value = '(CDHidsQXI*complexconjugate(CKM3x2))/(2.*LamX**2*cmath.sqrt(2)) + (CDHidsQX*complex(0,1)*complexconjugate(CKM3x2))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_347 = Coupling(name = 'GC_347',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM3x2))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM3x2))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_348 = Coupling(name = 'GC_348',
                  value = '(CDHiQuX*ee*complexconjugate(CKM3x2))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM3x2))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_349 = Coupling(name = 'GC_349',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM3x2))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM3x2))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM3x2))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM3x2))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_350 = Coupling(name = 'GC_350',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM3x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM3x2))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM3x2))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM3x2))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_351 = Coupling(name = 'GC_351',
                  value = '-0.25*(CDHiQsuXI*ee*vev*complexconjugate(CKM3x2))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM3x2))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_352 = Coupling(name = 'GC_352',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM3x2))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM3x2))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_353 = Coupling(name = 'GC_353',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM3x2))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM3x2))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM3x2))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM3x2))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_354 = Coupling(name = 'GC_354',
                  value = '-0.25*(CDHidsQXI*cw*ee*vev*complexconjugate(CKM3x2))/(LamX**2*sw*cmath.sqrt(2)) - (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM3x2))/(4.*LamX**2*sw*cmath.sqrt(2)) - (CDHidsQXI*ee*sw*vev*complexconjugate(CKM3x2))/(4.*cw*LamX**2*cmath.sqrt(2)) - (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM3x2))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_355 = Coupling(name = 'GC_355',
                  value = '(ee*complex(0,1)*complexconjugate(CKM3x3))/(sw*cmath.sqrt(2))',
                  order = {'QED':1})

GC_356 = Coupling(name = 'GC_356',
                  value = '(CXfQI*ee*complex(0,1)*complexconjugate(CKM3x3)*cmath.sqrt(2))/(LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_357 = Coupling(name = 'GC_357',
                  value = '-((CDHidQX*complexconjugate(CKM3x3))/(LamX**2*cmath.sqrt(2))) + (CDHidQXI*complex(0,1)*complexconjugate(CKM3x3))/(LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_358 = Coupling(name = 'GC_358',
                  value = '(CDHidsQXI*complexconjugate(CKM3x3))/(2.*LamX**2*cmath.sqrt(2)) + (CDHidsQX*complex(0,1)*complexconjugate(CKM3x3))/(2.*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_359 = Coupling(name = 'GC_359',
                  value = '-0.25*(CDHiQsuXI*ee*complexconjugate(CKM3x3))/(LamX**2*sw) + (CDHiQsuX*ee*complex(0,1)*complexconjugate(CKM3x3))/(4.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_360 = Coupling(name = 'GC_360',
                  value = '(CDHiQuX*ee*complexconjugate(CKM3x3))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*complexconjugate(CKM3x3))/(2.*LamX**2*sw)',
                  order = {'QED':1,'VBEFT':1})

GC_361 = Coupling(name = 'GC_361',
                  value = '-0.5*(CDHidQX*cw*ee*complexconjugate(CKM3x3))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*complexconjugate(CKM3x3))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*complexconjugate(CKM3x3))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*complexconjugate(CKM3x3))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_362 = Coupling(name = 'GC_362',
                  value = '(CDHidsQXI*cw*ee*complexconjugate(CKM3x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*complexconjugate(CKM3x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*complexconjugate(CKM3x3))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*complexconjugate(CKM3x3))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'QED':1,'VBEFT':1})

GC_363 = Coupling(name = 'GC_363',
                  value = '(CDHiQsuXI*ee*vev*complexconjugate(CKM3x3))/(4.*LamX**2*sw) - (CDHiQsuX*ee*complex(0,1)*vev*complexconjugate(CKM3x3))/(4.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_364 = Coupling(name = 'GC_364',
                  value = '(CDHiQuX*ee*vev*complexconjugate(CKM3x3))/(2.*LamX**2*sw) + (CDHiQuXI*ee*complex(0,1)*vev*complexconjugate(CKM3x3))/(2.*LamX**2*sw)',
                  order = {'VBEFT':1})

GC_365 = Coupling(name = 'GC_365',
                  value = '-0.5*(CDHidQX*cw*ee*vev*complexconjugate(CKM3x3))/(LamX**2*sw*cmath.sqrt(2)) + (CDHidQXI*cw*ee*complex(0,1)*vev*complexconjugate(CKM3x3))/(2.*LamX**2*sw*cmath.sqrt(2)) - (CDHidQX*ee*sw*vev*complexconjugate(CKM3x3))/(2.*cw*LamX**2*cmath.sqrt(2)) + (CDHidQXI*ee*complex(0,1)*sw*vev*complexconjugate(CKM3x3))/(2.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

GC_366 = Coupling(name = 'GC_366',
                  value = '(CDHidsQXI*cw*ee*vev*complexconjugate(CKM3x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQX*cw*ee*complex(0,1)*vev*complexconjugate(CKM3x3))/(4.*LamX**2*sw*cmath.sqrt(2)) + (CDHidsQXI*ee*sw*vev*complexconjugate(CKM3x3))/(4.*cw*LamX**2*cmath.sqrt(2)) + (CDHidsQX*ee*complex(0,1)*sw*vev*complexconjugate(CKM3x3))/(4.*cw*LamX**2*cmath.sqrt(2))',
                  order = {'VBEFT':1})

