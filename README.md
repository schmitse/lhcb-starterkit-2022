# lhcb-starterkit-2022

This repo contains a tutorial for the [`zfit`](https://github.com/zfit/zfit) and [`Minuit`](https://iminuit.readthedocs.io/en/stable/) libraries for parameter estimation in python that was created for the LHCb starterkit 2022. 

The lesson is divided into three different parts:
 - [Part I - zfit Basics](https://git.rwth-aachen.de/sebastian.schmitt1/lhcb-starterkit-2022/-/blob/main/zfitBasics.ipynb) sets the scene for the lesson and introduces the basics needed to run a fit in `zfit`. The fit result is investigated and different cost functions are introduced.
 - [Part II - zfit Fit Failure](https://git.rwth-aachen.de/sebastian.schmitt1/lhcb-starterkit-2022/-/blob/main/zfitFitFailure.ipynb) tries to give some examples as to why a fit might be unstable or fail and how to avoid them.
 - [Part III - zfit Advanced](https://git.rwth-aachen.de/sebastian.schmitt1/lhcb-starterkit-2022/-/blob/main/zfitAdvanced.ipynb) shows examples on more advanced use cases for `zfit`, like performing pseudoexperiments, statistical background subtraction, simultanous fits, and fits to a disjointed observable space. 

## Virtual environment

The notebook was created having `python 3.9` in mind with `zfit` version `0.10.1` and Minuit `2.17.0`.
Additionally required are the dependencies of the packages, such as `tensorflow`, and `numpy`. 
The way i recommend to set up a virtual environment for python is with [miniconda](https://docs.conda.io/en/latest/miniconda.html) or [micromamba](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html). The full requirements can be found in [requirements.txt](https://git.rwth-aachen.de/sebastian.schmitt1/lhcb-starterkit-2022/-/blob/main/requirements.txt). 

## Acknowledgements

Many thanks to Jonas Eschle for providing helpful comments when creating this tutorial and for his continued development of [`zfit`](https://github.com/zfit/zfit)!
Parts of this tutorial are inspired by [Hans Dembinskis pyHEP](https://nbviewer.org/github/HDembinski/PyHEP-2022-iminuit/blob/main/iminuit.ipynb) tutorial for `Minuit`. 