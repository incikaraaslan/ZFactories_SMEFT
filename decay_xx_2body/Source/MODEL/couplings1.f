ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1( )

      IMPLICIT NONE

      INCLUDE 'model_functions.inc'
      INCLUDE '../vector.inc'


      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_179 = (MDL_CW*MDL_CXHIB*MDL_COMPLEXI*MDL_VEV)/MDL_LAMX__EXP__2
      GC_184 = -((MDL_CXHIB*MDL_COMPLEXI*MDL_SW*MDL_VEV)
     $ /MDL_LAMX__EXP__2)
      GC_246 = -5.000000D-01*(MDL_CW__EXP__2*MDL_CXHIBI*MDL_EE
     $ *MDL_VEV__EXP__2)/(MDL_LAMX__EXP__2*MDL_SW)-(MDL_CXHIBI*MDL_EE
     $ *MDL_SW*MDL_VEV__EXP__2)/(2.000000D+00*MDL_LAMX__EXP__2)
      GC_248 = (MDL_CW*MDL_CXHIBI*MDL_EE*MDL_VEV__EXP__2)/(2.000000D
     $ +00*MDL_LAMX__EXP__2)+(MDL_CXHIBI*MDL_EE*MDL_SW__EXP__2
     $ *MDL_VEV__EXP__2)/(2.000000D+00*MDL_CW*MDL_LAMX__EXP__2)
      END
