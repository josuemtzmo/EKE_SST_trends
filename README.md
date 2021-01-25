# Global changes in oceanic mesoscale currents over the satellite altimetry record

| Zenodo |
|:------:|
|[![DOI](https://zenodo.org/badge/289187055.svg)](https://zenodo.org/badge/latestdoi/289187055)|

A repository containing material related to the manuscript

> Martínez-Moreno, J., Hogg, A. McC., England, M. H., Constantinou, N. C., Kiss, A. E., and Morrison, A. K. Global changes in oceanic mesoscale currents over the satellite altimetry record. (submitted on Oct. 2020; preprint available at doi:[10.21203/rs.3.rs-88932/v1](https://doi.org/10.21203/rs.3.rs-88932/v1))

that investigates the temporal evolution of oceanic surface eddy kinetic energy and sea surface temperature over the satellite record from a global, geographical and dynamical-region perspective.

Analysed datasets include the [AVISO+ SSH altimetry](https://www.aviso.altimetry.fr/en/data/products/sea-surface-height-products/global/gridded-sea-level-heights-and-derived-variables.html) and [NOAA optimal interpolated sea surface temperature](https://www.ncdc.noaa.gov/oisst) (OISST). 

### Python requirements:

Make sure you have the required dependencies installed (`numpy`, `xarray`,`dask`,`cartopy`,`cmocean`, & `jupyterlab`):

```
pip install -r requirements.txt 
```

```
conda install -c conda-forge --file ./requirements.txt
```

Additionally, install [xarrayMannKendall](https://github.com/josuemtzmo/xarrayMannKendall):

```
git clone https://github.com/josuemtzmo/xarrayMannKendall.git
```

and follow the installation instructions in [xarrayMannKendall GitHub Page](https://github.com/josuemtzmo/xarrayMannKendall).

### Contents:

[`manuscript`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/manuscript): folder containing the LaTeX source files and figures for the manuscript

[`datasets`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/datasets): folder in which the NetCDF (.nc) output files are expected to be found. Download NetCDF files from <a href="https://doi.org/10.5281/zenodo.3993823"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.3993823.svg" alt="zenodo doi"></a>

[`figures`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/figures): folder with jupyter notebooks that produce the main figures of the manuscript.

[`pre-processing`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/pre-processing): folder with scripts and instructions that reproduce `.nc` files in `datasets` from the raw AVISO+ dataset

[`trends`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/trends): folder with jupyter notebooks that compute trends

### Datasets:

To generate all the pre-processed [`datasets`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/datasets) of this repository, you need access to the AVISO+ altimetry and OISST NOAA datasets for period Jan. 1993 - Dec 2019. The generated pre-processed datasets will reproduce the analysis and results presented in the manuscript. All the required notebooks to reproduce the pre-processed datasets from the raw AVISO+ and OISST NOAA datasets are in the [`pre-processing`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/pre-processing) and [`trends`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/trends) folders. The notebooks within `pre-processing` folder use the raw satellite output to produce some of the `.nc` files inside `datasets`; the notebooks within `trends` use the `.nc` files in `datasets` that were produced by `pre-processing` to output the `*_trends.nc` files inside `datasets`.

Execute the notebooks in the following order:

1. `./pre-processing/AVISO+_to_EKE_timeseries.ipynb`: generate the EKE field `(lon, lat, time)` from the AVISO+ geostrophic velocity anomalies.
2. `./pre-processing/OISST_to_SST_grad_timeseries.ipynb`; generate the SST gradient field `(lon, lat, time)` from the OISST NOAA SST record.
3. `./pre-processing/KE_anomaly_timeseries.ipynb`; generate the KE field anomaly `(lon, lat, time)` from the AVISO+ geostrophic velocities.
4. `./pre-processing/EKE_scale_decomposition.ipynb`; use a 3°x 3° kernel to decompose the EKE field `(lon, lat, time)` into large-scale EKE and mesoscale EKE.
5. `./pre-processing/SST_gradient_scale_decomposition.ipynb`; use a 3°x 3° kernel to decompose the SST gradient field `(lon, lat, time)` into large-scale SST gradients and mesoscale SST gradients (features smaller than 3°x 3° degrees).
6. Subsequently, the trends can be reproduced by executing the notebooks in the folder `trends`. 
7. Download mask into the `datasets` folder:
    ```
    cd datasets 
    wget https://zenodo.org/record/3993824/files/ocean_basins_and_dynamical_masks.nc?download=1
    ```

Optionally, if you do not have access to AVISO+ or OISST NOAA datasets, you can download the pre-processed datasets from  <a href="https://doi.org/10.5281/zenodo.3993823"><img src="https://zenodo.org/badge/DOI/10.5281/zenodo.3993823.svg" alt="zenodo doi"></a>. To facilitate the download of all `*.nc` files, fist install <a href="https://doi.org/10.5281/zenodo.3993824">zenodo_get</a>:

```
pip install zenodo-get
```

Then all the datasets can be downloaded via:

```
cd datasets
zenodo_get 10.5281/zenodo.3993824
```

> **WARNING**: Disk space of ~17 GB is required to download all contents of `datasets` folder.

Now you can reproduce all the analysis and figures of the manuscript; see [`figures`](https://github.com/josuemtzmo/EKE_SST_trends/tree/master/figures) folder.

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

>Josué Martínez Moreno, Andrew McC. Hogg, Matthew H. England, Navid C. Constantinou, Andrew E. Kiss, & Adele K. Morrison. (2021, January 23). josuemtzmo/EKE_SST_trends: EKE_SST_trends: Jupyter notebooks (Python) used to compute trends of Eddy kinetic energy and sea surface temperature (Version v0.1.0-alpha). Zenodo. http://doi.org/10.5281/zenodo.4458783

### Software reference:
- David Völgyes, & Rick Lupton. (2020, February 20). Zenodo_get: a downloader for Zenodo records (Version v1.3.0). Zenodo. http://doi.org/10.5281/zenodo.3676567
- Josué Martínez Moreno, & Navid C. Constantinou. (2021, January 23). josuemtzmo/xarrayMannKendall: Mann Kendall significance test implemented in xarray. (Version v.1.0.1). Zenodo. http://doi.org/10.5281/zenodo.4458776
