import matplotlib.pyplot as plt
import numpy as np
import boost_histogram as bh
import zfit

def plot_fit(dat: np.ndarray, basis: np.ndarray, model: np.ndarray, 
             obs: zfit.Space, nbins : int=50, smodel: np.ndarray=None,
             drawstyle: str='default'):
    """
    quick plotting function to visualise data and model. 
    Takes:
     - dat: (array) the data that are fitted
     - basis: (array) the points at which the model is evaluated
     - model: (array) the model that describes the data
     - obs: (zfit Space) the space in which the model lives
     - nbins: (int) the number of bins for the data histogram
     - smodel: (array) uncertainty on model (not needed)
     - drawstyle: (str) the drawstyle of plt.plot
    Returns:
     - None
    """
    # for normalising the pdf, scaled pdf = pdf * yield * area / bins
    limits = obs.limits 
    area = obs.area().numpy()

    # data in histogram over the full observable space
    hist = bh.Histogram(bh.axis.Regular(nbins, *limits))
    hist.fill(dat)

    # the figure with an errorbar for the data and a line for the model
    fig, ax = plt.subplots()
    art_data = ax.errorbar(hist.axes.centers[0], hist.values(), 
                           xerr=hist.axes.widths[0]/2,
                           yerr=np.sqrt(hist.values()), fmt='.', 
                           label='Data', color='black', zorder=10)
    art_model = ax.plot(basis, model * area/nbins, color='darkturquoise', 
                        label='Model', zorder=8, drawstyle=drawstyle)[0]
    
    # if we have the uncertainty on the model we draw it as contour
    # and update the artist for the legend to reflect on the new model
    if smodel is not None:
        _art = ax.fill_between(basis, (model+smodel)*area/nbins, 
                               (model-smodel)*area/nbins, color='darkturquoise', 
                               alpha=0.5, zorder=-2)
        art_model = (art_model, _art)
        
    # legend and axis labels
    ax.legend((art_data, art_model), ('Data', 'Model'), loc='best', 
              title='LHCb Starterkit', title_fontsize=12)
    ax.set_xlabel('Observable')
    ax.set_ylabel('Counts [a.u.]');
