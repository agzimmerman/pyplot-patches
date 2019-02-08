import math


def loglog_lims_with_axis_equal(axes, xlim, ylim):
    """ Set axes to loglog with equal spacing and specified limits.
    This is needed because the combination of loglog, axis("equal"), and xlim
    does not work correctly with pyplot.
    """
    assert(len(xlim) == 2)
    
    assert(len(ylim) == 2)
    
    axes.set_xscale("log")
    
    axes.set_yscale("log")
    
    axes.set_xlim(xlim)
    
    axes.set_ylim(ylim)
    
    log = math.log
    
    log_scale = (log(ylim[1]) - log(ylim[0]))/(log(xlim[1]) - log(xlim[0]))
    
    log10 = math.log10
    
    power_scale = (log10(ylim[1]) - log10(ylim[0]))/  \
        (log10(xlim[1]) - log10(xlim[0]))
    
    axes.set_aspect(log_scale/power_scale)
    