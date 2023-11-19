$# LS-DYNA Keyword file created by LS-PrePost(R) V4.10.4-22May2023
$# Created on Nov-19-2023 (18:52:34)
*KEYWORD
*TITLE
$#                                                                         title
LS-DYNA keyword deck by LS-PrePost
*CONTROL_IMPLICIT_AUTO
$         0        10         3       0.0      0.01       0.0         0         0
$#   iauto    iteopt    itewin     dtmin     dtmax     dtexp     kfail    kcycle
         1        25         5     0.001      0.01       0.0         0         0
*CONTROL_IMPLICIT_DYNAMICS
$#   imass     gamma      beta    tdybir    tdydth    tdybur     irate     alpha
         1      0.55      0.28       0.0       0.0       0.0         2       0.0
*CONTROL_IMPLICIT_GENERAL
$#  imflag       dt0    imform      nsbs       igs     cnstn      form    zero_v
         1     0.005         2         1         2         0         0         0
*CONTROL_IMPLICIT_SOLUTION
$#  nsolvr    ilimit    maxref     dctol     ectol     rctol     lstol    abstol
        12         5        40     0.001      0.011.00000E10       0.91.0000E-10
$#   dnorm    diverg     istif   nlprint    nlnorm   d3itctl     cpchk
         2         1         1         0         0         0         0
$#  arcctl    arcdir    arclen    arcmth    arcdmp    arcpsi    arcalf    arctim
         0         0       0.0         1         2       0.0       0.0       0.0
$#   lsmtd     lsdir      irad      srad      awgt      sred
         4         2       0.0       0.0       0.0       0.0
*CONTROL_TERMINATION
$#  endtim    endcyc     dtmin    endeng    endmas     nosol
       2.0         0       0.0       0.01.000000E8         0
*DATABASE_ELOUT
$#      dt    binary      lcur     ioopt   option1   option2   option3   option4
      0.01         0         0         1         0         0         0         0
*DATABASE_NODFOR
$#      dt    binary      lcur     ioopt
      0.01         3         0         1
*DATABASE_NODOUT
$#      dt    binary      lcur     ioopt   option1   option2
      0.01         3         0         1       0.0         0
*DATABASE_SLEOUT
$#      dt    binary      lcur     ioopt
      0.01         0         0         1
*DATABASE_BINARY_D3PLOT
$#      dt      lcdt      beam     npltc    psetid
      0.01         0         0         0         0
$#   ioopt      rate    cutoff    window      type      pset
         0       0.0       0.0       0.0         0         0
*DATABASE_BINARY_INTFOR_FILE
$#                                                                      filename
intforc
$#      dt      lcdt      beam     npltc    psetid
      0.01         0         0         0         0
*DATABASE_EXTENT_BINARY
$#   neiph     neips    maxint    strflg    sigflg    epsflg    rltflg    engflg
         0         0         3         1         1         1         1         1
$#  cmpflg    ieverp    beamip     dcomp      shge     stssz    n3thdt   ialemat
         0         0         0         1         1         1         2         1
$# nintsld   pkp_sen      sclp     hydro     msscl     therm    intout    nodout
         0         0       1.0         0         0         0                    
$#    dtdt    resplt     neipb   quadsld    cubsld   deleres
         0         0         0         0         0         0
*DATABASE_FORMAT
$#   iform   ibinary
         0         1
*DATABASE_NODAL_FORCE_GROUP
$#    nsid       cid
         2         0
*BOUNDARY_PRESCRIBED_MOTION_SET_ID
$#      id                                                               heading
         1compression displacement
$#    nsid       dof       vad      lcid        sf       vid     death     birth
         1         2         2         1       1.0         01.00000E28       0.0
*BOUNDARY_SPC_SET
$#    nsid       cid      dofx      dofy      dofz     dofrx     dofry     dofrz
         2         0         1         1         1         1         1         1
*SET_NODE_GENERAL_TITLE
bottom boundary nodes defined by bottom box
$#     sid       da1       da2       da3       da4    solver       its         -
         2       0.0       0.0       0.0       0.0MECH      1                   
$#  option        e1        e2        e3        e4        e5        e6        e7
BOX                2         0         0         0         0         0         0
*BOUNDARY_SPC_SET
$#    nsid       cid      dofx      dofy      dofz     dofrx     dofry     dofrz
         0         0         0         0         0         0         0         0
         1         0         1         0         1         0         0         0
*SET_NODE_GENERAL_TITLE
top boundary nodes defined by top box
         1       0.0       0.0       0.0       0.0MECH      1                   
BOX                1         0         0         0         0         0         0
*BOUNDARY_SPC_SET
$#    nsid       cid      dofx      dofy      dofz     dofrx     dofry     dofrz
         2         0         1         1         1         1         1         1
*CONTACT_AUTOMATIC_SINGLE_SURFACE_MORTAR_ID
$#     cid                                                                 title
         1                                                                      
$#   surfa     surfb  surfatyp  surfbtyp   saboxid   sbboxid      sapr      sbpr
         0         0         0         0         0         0         0         0
$#      fs        fd        dc        vc       vdc    penchk        bt        dt
       0.2       0.2       0.0       0.0       0.0         0       0.01.00000E20
$#    sfsa      sfsb      sast      sbst     sfsat     sfsbt       fsf       vsf
       1.0       1.0       0.0       0.0       1.0       1.0       1.0       1.0
*MAT_ELASTIC_TITLE
aluminium
$#     mid        ro         e        pr        da        db  not used
         12.70000E-6      70.0       0.3       0.0       0.0       0.0
*SECTION_BEAM_TITLE
beam section
$#   secid    elform      shrf   qr/irid       cst     scoor       nsm     naupd
         1         1       1.0         2         1       0.0       0.0         0
$#     ts1       ts2       tt1       tt2     nsloc     ntloc
       0.4       0.4       0.0       0.0       0.0       0.0
*DEFINE_BOX_TITLE
top boundary box
$#   boxid       xmn       xmx       ymn       ymx       zmn       zmx
         1     -10.0      10.0       5.8      10.0     -10.0      10.0
*DEFINE_BOX_TITLE
bot boundary box
$#   boxid       xmn       xmx       ymn       ymx       zmn       zmx
         2     -10.0      10.0     -10.0      -5.8     -10.0      10.0
*DEFINE_CURVE_TITLE
Displacement Curve
$#    lcid      sidr       sfa       sfo      offa      offo    dattyp     lcint
         1         0       1.0       1.0       0.0       0.0         0         0
$#                a1                  o1
                 0.0                 0.0
                 1.0                -5.5
                 2.0                 0.0
                 3.0                 0.0
*CONSTRAINED_GLOBAL
$#      tc        rc       dir         x         y         z       tol
         3         0         3       0.0       0.0       0.0      10.0
*NODE_MERGE_SET
$#    nsid
         3
*NODE_MERGE_TOLERANCE
$#    tolr
      0.05
*INCLUDE
beams.k
*SET_NODE_GENERAL_TITLE
all nodes
$#     sid       da1       da2       da3       da4    solver       its         -
         3       0.0       0.0       0.0       0.0MECH      1                   
$#  option        e1        e2        e3        e4        e5        e6        e7
PART               1         0         0         0         0         0         0
*END
