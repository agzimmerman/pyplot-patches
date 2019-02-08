import math


def loglog_lims_with_axis_equal(axes, xlim, ylim):
    """ Set axes to loglog with equal spacing and specified limits.
    This is needed because the combination of loglog, axis("equal"), and xlim
    does not work correctly with pyplot.
    """
    for lim, set_scale, set_lim in zip(
            (xlim, ylim), 
            (axes.set_xscale, axes.set_yscale),
            (axes.set_xlim, axes.set_ylim)):
    
        assert(len(lim) == 2)
    
        set_scale("log")
    
        set_lim(lim)
    
    scales = []
    
    for log in (math.log, math.log10):
    
        scales.append((log(ylim[1]) - log(ylim[0]))/  \
            (log(xlim[1]) - log(xlim[0])))
    
    axes.set_aspect(scales[0]/scales[1])
    