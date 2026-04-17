def selection_8():

    # Library import
    import numpy
    import matplotlib
    import matplotlib.pyplot   as plt
    import matplotlib.gridspec as gridspec

    # Library version
    matplotlib_version = matplotlib.__version__
    numpy_version      = numpy.__version__

    # Histo binning
    xBinning = numpy.linspace(-10.0,10.0,41,endpoint=True)

    # Creating data sequence: middle of each bin
    xData = numpy.array([-9.75,-9.25,-8.75,-8.25,-7.75,-7.25,-6.75,-6.25,-5.75,-5.25,-4.75,-4.25,-3.75,-3.25,-2.75,-2.25,-1.75,-1.25,-0.75,-0.25,0.25,0.75,1.25,1.75,2.25,2.75,3.25,3.75,4.25,4.75,5.25,5.75,6.25,6.75,7.25,7.75,8.25,8.75,9.25,9.75])

    # Creating weights for histo: y9_ETA_0
    y9_ETA_0_weights = numpy.array([0.0,0.0,0.0,0.0,0.0,0.0,0.0003678024706018292,0.0007356049412036584,0.002206815023535241,0.0062526424000796275,0.015079897496113952,0.03825145794221156,0.06804345406247442,0.13498346612624543,0.19714211944439808,0.23208338314059035,0.25893291211398767,0.28872492642735864,0.2946097971451734,0.2931385544751865,0.3122643093364847,0.2780586669752858,0.28284005570954396,0.27107041423604733,0.23833601454483538,0.18831486334874242,0.1327767020833979,0.07356049412036585,0.039354868152956766,0.015447704564973887,0.00662044427090866,0.003310222035492197,0.0007356049412036584,0.0,0.0003678024706018292,0.0,0.0,0.0,0.0,0.0])

    # Creating a new Canvas
    fig   = plt.figure(figsize=(8.75,6.25),dpi=80)
    frame = gridspec.GridSpec(1,1)
    pad   = fig.add_subplot(frame[0])

    # Creating a new Stack
    pad.hist(x=xData, bins=xBinning, weights=y9_ETA_0_weights,\
             label="$run\_01$", histtype="stepfilled", rwidth=1.0,\
             color="#5954d8", edgecolor="#5954d8", linewidth=1, linestyle="solid",\
             bottom=None, cumulative=False, density=False, align="mid", orientation="vertical")


    # Axis
    plt.rc('text',usetex=False)
    plt.xlabel(r"$\eta$ $[ mu+_{1} ]$ ",\
               fontsize=16,color="black")
    plt.ylabel(r"$\mathrm{Events}$ $(\mathcal{L}_{\mathrm{int}} = 10\ \mathrm{fb}^{-1})$ ",\
               fontsize=16,color="black")

    # Boundary of y-axis
    ymax=(y9_ETA_0_weights).max()*1.1
    #ymin=0 # linear scale
    ymin=min([x for x in (y9_ETA_0_weights) if x])/100. # log scale
    plt.gca().set_ylim(ymin,ymax)

    # Log/Linear scale for X-axis
    plt.gca().set_xscale("linear")
    #plt.gca().set_xscale("log",nonpositive="clip")

    # Log/Linear scale for Y-axis
    #plt.gca().set_yscale("linear")
    plt.gca().set_yscale("log",nonpositive="clip")

    # Saving the image
    plt.savefig('../../HTML/MadAnalysis5job_0/selection_8.png')

# Running!
if __name__ == '__main__':
    selection_8()
