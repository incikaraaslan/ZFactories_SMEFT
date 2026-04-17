ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

C     
C     NB: VECSIZE_MEMMAX is defined in vector.inc
C     NB: vector.inc must be included before coupl.inc
C     

      DOUBLE PRECISION G, ALL_G(1)
      COMMON/STRONG/ G, ALL_G

      DOUBLE COMPLEX GAL(2)
      COMMON/WEAK/ GAL

      DOUBLE PRECISION MU_R, ALL_MU_R(1)
      COMMON/RSCALE/ MU_R, ALL_MU_R

      DOUBLE PRECISION NF
      PARAMETER(NF=4D0)
      DOUBLE PRECISION NL
      PARAMETER(NL=2D0)

      DOUBLE PRECISION MDL_MB,MDL_MH,MDL_MH1,MDL_MT,MDL_MT1,MDL_MTA
     $ ,MDL_MW,MDL_MW1,MDL_MZ,MDL_MZ1

      COMMON/MASSES/ MDL_MB,MDL_MH,MDL_MH1,MDL_MT,MDL_MT1,MDL_MTA
     $ ,MDL_MW,MDL_MW1,MDL_MZ,MDL_MZ1


      DOUBLE PRECISION MDL_WH,MDL_WH1,MDL_WT,MDL_WT1,MDL_WW,MDL_WW1
     $ ,MDL_WZ,MDL_WZ1

      COMMON/WIDTHS/ MDL_WH,MDL_WH1,MDL_WT,MDL_WT1,MDL_WW,MDL_WW1
     $ ,MDL_WZ,MDL_WZ1


      DOUBLE COMPLEX GC_5899, GC_5909, GC_5911, GC_6185, GC_6186,
     $  GC_6637, GC_6641, GC_7444, GC_7557

      COMMON/COUPLINGS/ GC_5899, GC_5909, GC_5911, GC_6185, GC_6186,
     $  GC_6637, GC_6641, GC_7444, GC_7557

