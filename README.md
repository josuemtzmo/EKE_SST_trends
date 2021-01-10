# Global changes in oceanic mesoscale currents over the satellite altimetry record

A repository containing material related to the manuscript

> Martínez-Moreno, J., Hogg, A. McC., England, M. H., Constantinou, N. C., Kiss, A. E., and Morrison, A. K. Global changes in oceanic mesoscale currents over the satellite altimetry record. (submitted on Oct. 2020; preprint at doi:[10.21203/rs.3.rs-88932/v1](https://doi.org/10.21203/rs.3.rs-88932/v1))

that investigates the temporal evolution of oceanic surface eddy kinetic energy and sea surface temperature over the satellite record from a global, geographical and dynamical-region perspective.


Analysed datasets include the [AVISO+ SSH altimetry](https://www.aviso.altimetry.fr/en/data/products/sea-surface-height-products/global/gridded-sea-level-heights-and-derived-variables.html) and [NOAA optimal interpolated sea surface temperature](https://www.ncdc.noaa.gov/oisst) (OISST). 

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

### Contents

`trends`: folder with jupyter notebooks that compute trends. [to be added]

`figures`: folder with jupyter notebooks that produce the main figures of the manuscript. [to be added]

`data`: folder in which the NetCDF (`.nc`) output files are expected to be found. Download NetCDF files from doi:[10.5281/zenodo.3993824](https://doi.org/10.5281/zenodo.3993824).

Contributors:
[Josué Martínez-Moreno](http://josuemtzmo.github.io/) (@josuemtzmo), 
[Andy McC. Hogg](http://rses.anu.edu.au/people/academics/prof-andy-hogg) (@AndyHoggANU), 
[Matthew H. England](http://web.science.unsw.edu.au/~matthew/), 
[Navid C. Constantinou](http://www.navidconstantinou.com) (@navidcy),
[Andrew E. Kiss](https://researchers.anu.edu.au/researchers/kiss-ae) (@aekiss),
[Adele K. Morrison](http://rses.anu.edu.au/people/academics/dr-adele-morrison) (@adele157).
