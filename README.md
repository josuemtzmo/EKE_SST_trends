# Global changes in oceanic mesoscale currents over the satellite altimetry record
| Zenodo |
|:------:|
|[![DOI](https://zenodo.org/badge/289187055.svg)](https://zenodo.org/badge/latestdoi/289187055)|

A repository containing material related to the manuscript

> Martínez-Moreno, J., Hogg, A. McC., England, M. H., Constantinou, N. C., Kiss, A. E., and Morrison, A. K. Global changes in oceanic mesoscale currents over the satellite altimetry record. (submitted on Oct. 2020; preprint at doi:[10.21203/rs.3.rs-88932/v1](https://doi.org/10.21203/rs.3.rs-88932/v1))

that investigates the temporal evolution of oceanic surface eddy kinetic energy and sea surface temperature over the satellite record from a global, geographical and dynamical-region perspective.


Analysed datasets include the [AVISO+ SSH altimetry](https://www.aviso.altimetry.fr/en/data/products/sea-surface-height-products/global/gridded-sea-level-heights-and-derived-variables.html) and [NOAA optimal interpolated sea surface temperature](https://www.ncdc.noaa.gov/oisst) (OISST). 

## Abstract

Oceanic mesoscale eddies play a profound role in mixing tracers such as heat, carbon, and nutrients, thereby regulating regional and global climate. Yet, it remains unclear how the eddy field has varied over the past few decades. Furthermore, climate model predictions generally do not resolve mesoscale eddies, which could limit their accuracy in simulating future climate change. Here we show a global statistically significant increase of ocean eddy activity using two independent observational datasets of surface mesoscale eddy variability, one estimates surface currents and the other is derived from sea surface temperature. Maps of mesoscale variability trends show heterogeneous patterns, with eddy-rich regions showing a significant increase of 2% - 5% per decade, while the tropical oceans show a decrease in mesoscale variability. This readjustment of the surface mesoscale ocean circulation has important implications for the exchange of heat and carbon between the ocean and atmosphere.

### Python requirements:

Make sure you have the module requirements (`numpy`, `xarray`,`dask`,`cartopy`,`cmocean`, & `jupyterlab`):

```
pip install -r requirements.txt 
```

```
conda install -c conda-forge --file ./requirements.txt
```

Aditionally, install [xarrayMannKendall](https://github.com/josuemtzmo/xarrayMannKendall):

```
git clone https://github.com/josuemtzmo/xarrayMannKendall.git
```

and follow the installation instructions in [xarrayMannKendall GitHub Page](https://github.com/josuemtzmo/xarrayMannKendall).

### Contents:

[`manuscript`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/manuscript): folder containing the LaTeX source files and figures for the manuscript

[`datasets`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/datasets): folder in which the NetCDF (.nc) output files are expected to be found. Download NetCDF files from <a href="https://doi.org/10.5281/zenodo.3993824"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.3993824.svg" alt="zenodo doi"></a>

[`figures`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/figures): folder with jupyter notebooks that produce the main figures of the manuscript.

[`pre-processing`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/pre-processing): folder with scripts and instructions that reproduce `.nc` files in `datasets` from the raw AVISO+ dataset

[`trends`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/trends): folder with jupyter notebooks that compute trends

### Authors:
- [Josué Martínez-Moreno](http://josuemtzmo.github.io/) (@josuemtzmo) <[josue.martinezmoreno@anu.edu.au](mailto:josue.martinezmoreno@anu.edu.au)>, 
- [Andy McC. Hogg](http://rses.anu.edu.au/people/academics/prof-andy-hogg) (@AndyHoggANU), 
- [Matthew H. England](http://web.science.unsw.edu.au/~matthew/), 
- [Navid C. Constantinou](http://www.navidconstantinou.com) (@navidcy),
- [Andrew E. Kiss](https://researchers.anu.edu.au/researchers/kiss-ae) (@aekiss),
- [Adele K. Morrison](http://rses.anu.edu.au/people/academics/dr-adele-morrison) (@adele157).

### Funding:
This study was supported by the ARC Centre of Excellence for Climate Extremes, Australia. (CLEX), in addition to the authors been suported by:
- J.M.‐M. was supported by the Consejo Nacional de Ciencia y Tecnología (CONACYT), Mexico funding. 
- M.H.E. was supported by the Centre for Southern Hemisphere Oceans Research (CSHOR), a joint research centre between QNLM, CSIRO, UNSW and UTAS.
- A.K.M. was supported by the Australian Research Council DECRA Fellowship

### Cite this code:

This repository can be cited as:

Josué Martínez Moreno, Andrew McC. Hogg, Matthew H. England, Navid C. Constantinou, Andrew E. Kiss, & Adele K. Morrison. (2021, January 23). josuemtzmo/EKE_SST_trends: EKE_SST_trends: Jupyter notebooks (Python) used to compute trends of Eddy kinetic energy and sea surface temperature (Version v0.1.0-alpha). Zenodo. http://doi.org/10.5281/zenodo.4458784
