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
      GC_6361 = (2.000000D+00*MDL_COMPLEXI*MDL_GHZA)/MDL_VEVHAT
      GC_6505 = (MDL_CEBRE13*MDL_CTH*MDL_COMPLEXI*MDL_VEVHAT)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2)
      GC_6509 = (MDL_CEBRE31*MDL_CTH*MDL_COMPLEXI*MDL_VEVHAT)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2)
      GC_6738 = (MDL_EE__EXP__2*MDL_COMPLEXI*MDL_VEVHAT)/(2.000000D+00
     $ *MDL_CTH__EXP__2*MDL_STH__EXP__2)
      GC_7006 = -((MDL_CEBRE13*MDL_COMPLEXI*MDL_STH*MDL_VEVHAT)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2))
      GC_7010 = -((MDL_CEBRE31*MDL_COMPLEXI*MDL_STH*MDL_VEVHAT)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2))
      GC_7743 = -((MDL_COMPLEXI*MDL_YTAU)/MDL_SQRT__2)
      GC_6205 = -((MDL_CEBRE13*MDL_COMPLEXI*MDL_STH)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2))
      GC_6209 = -((MDL_CEBRE31*MDL_COMPLEXI*MDL_STH)
     $ /(MDL_LAMBDASMEFT__EXP__2*MDL_SQRT__2))
      END
