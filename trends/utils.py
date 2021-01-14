import numpy as np

import matplotlib.patches as mpatches
import cartopy.crs as ccrs
import cartopy.feature as feature

# Constant:
earth_radius = 6371e3
omega = 7.2921159e-5

# Function to compute grid area:
def area(lat,lon):
    """
    Compute area of a rectilinear grid.
    """
    lat_r = np.radians(lat)
    lon_r = np.radians(lon)
    f=2*omega*np.sin(lat_r)
    grad_lon=lon_r.copy()
    grad_lon.data=np.gradient(lon_r)

    dx=grad_lon*earth_radius*np.cos(lat_r)
    dy=np.gradient(lat_r)*earth_radius

    return dx*dy
    
    
def add_patches(axis):
    """
    Add patches over the Black Sea and Caspian Sea.
    """
    axis.add_patch(mpatches.Rectangle(xy=[27, 38], width=20, height=10,
                                    facecolor='#DFD1AF',
                                    alpha=1,
                                    zorder=3,
                                    transform=ccrs.Geodetic()))

    axis.add_patch(mpatches.Rectangle(xy=[38, 36], width=20, height=11,
                                    facecolor='#DFD1AF',
                                    alpha=1,
                                    zorder=3,
                                    transform=ccrs.Geodetic()))

    
ccrs_land = feature.NaturalEarthFeature('physical', 'land', '50m',
                                        edgecolor='black',
                                        facecolor='#DFD1AF',
                                        linewidth=0.2)