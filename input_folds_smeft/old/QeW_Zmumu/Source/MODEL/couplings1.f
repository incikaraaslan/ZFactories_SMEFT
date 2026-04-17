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
      GC_5909 = -(MDL_EE*MDL_COMPLEXI)/(2.000000D+00*MDL_CTH*MDL_STH)
      GC_6187 = -((MDL_EE*MDL_COMPLEXI*MDL_STH)/MDL_CTH)
      GC_6531 = -((MDL_CEWRE22*MDL_CTH*MDL_COMPLEXI*MDL_VEVHAT)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2))
      END
