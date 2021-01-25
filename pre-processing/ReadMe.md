# Pre-processing

To generate all the pre-processed datasets of this repository [10.5281/zenodo.3993824](https://doi.org/10.5281/zenodo.3993824), it is required to have full access to the AVISO+ dataset and OISST NOAA (1993-2020), the generated pre-processed datasets will reproduce the analysis and results presented in the Martínez-Moreno, J, _et al._ 2020. All the required notebooks to reproduce these datasets are located in the `pre-processing` and `trends` folders. 
Execute the notebooks in the following order:

1. `./pre-processing/AVISO+_to_EKE_timeseries.ipynb`; This notebook generates the EKE field (lon,lat,t) from the AVISO+ geostrophic velocities anomalies.
2. `./pre-processing/OISST_to_SST_grad_timeseries.ipynb`; This notebook generates the SST gradient field (lon,lat,t) from the OISST NOAA SST field.
3. `./pre-processing/KE_anomaly_timeseries.ipynb`; This notebook generates the KE field anomaly (lon,lat,t) from the AVISO+ geostrophic velocities.
4. `./pre-processing/EKE_scale_decomposition.ipynb`; This notebook decomposes the EKE field (lon,lat,t) into large-scale EKE and mesoscale EKE (features smaller than 3°x 3° degrees).
5. `./pre-processing/SST_gradient_scale_decomposition.ipynb`; This notebook decomposes the SST gradient field (lon,lat,t) into large-scale SST gradients and mesoscale SST gradients (features smaller than 3°x 3° degrees).
6. Subsequently, the trends can be reproduced by executing the notebooks in the folder `trends`. 
7. Download mask into the `datasets` folder:
    ```cd ../datasets; wget https://zenodo.org/record/3993824/files/ocean_basins_and_dynamical_masks.nc?download=1```
