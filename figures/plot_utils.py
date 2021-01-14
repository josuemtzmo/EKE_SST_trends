import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

import cartopy.crs as ccrs
import cartopy.feature as feature
import cmocean as cm
import matplotlib.ticker as mticker

from scipy import stats
from xarrayMannKendall import Mann_Kendall_test

earth_radius = 6371e3
omega = 7.2921159e-5

def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    """
    Truncate colormap.
    """
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap

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

import matplotlib.patches as mpatches

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

def vectorize(cs):
    """
    Vectorize contourf plots to reduce weight of figures saved as PDFs.
    """
    for c in cs.collections:
        c.set_rasterized(True)
        
def plot_region(ax, SST_trend, EKE_trend, region):
    """
    Plot SST trends and EKE contours in a given region. 
    """
    clm = SST_trend.plot.contourf(vmin = -2e-6, vmax = 2e-6, levels = np.round(np.linspace(-2e-6,2e-6,16),7), 
                              extend = 'both', transform = ccrs.PlateCarree(), add_colorbar = False,
                              cmap = truncate_colormap(cm.cm.balance, 0.1, 0.9), ax=ax)
    
    ax.set_extent(region, crs=ccrs.PlateCarree())
    ax.add_feature(ccrs_land, zorder=2)
    
    ax.spines['geo'].set_linewidth(0.5)

    ax.set_title("",fontsize=8)
    gl = ax.gridlines(linewidth=0.2)

    gl.xlocator = mticker.FixedLocator(range(-180,181,40))
    gl.ylocator = mticker.FixedLocator(range(-60,61,30))

    cs = EKE_trend.plot.contour(levels=[-5,5],transform=ccrs.PlateCarree(),linewidths=0.8,colors='k')
    
    vectorize(cs)
    vectorize(clm)
    
    return clm, cs

def plot_bars(ax,x,slope,error,width=0.1,**kwargs):
    ax.plot([x,x],[slope-error/2,slope+error/2],**kwargs)
    ax.plot([x-(x/x)*width,x+(x/x)*width],[slope-error/2,slope-error/2],**kwargs)
    ax.plot([x-(x/x)*width,x+(x/x)*width],[slope+error/2,slope+error/2],**kwargs)
    
def plot_ocean_basins(ax,ocean_basins):
    counter=0
    colorbars=['cool','Greens','Greys','Blues']
    for ii in ocean_basins.data_vars:
        if 'ocean' in ii:
            ocean_basins[ii].where(ocean_basins[ii]==True).plot.contourf(transform=ccrs.PlateCarree(),
                                                                         cmap=colorbars[counter]+'_r',
                                                                         alpha=0.8,add_colorbar=False,
                                                                         vmin=0,vmax=2)
            counter+=1
    ax.set_global()

    ax.add_feature(ccrs_land, zorder=1)
    ax.spines['geo'].set_linewidth(1)

    ax.plot([1, 359], [9, 9],
             color='k', linewidth=0.5, linestyle='--',
             transform=ccrs.PlateCarree(),zorder=0
             )

    ax.plot([1, 359], [-9, -9],
             color='k', linewidth=0.5, linestyle='--',
             transform=ccrs.PlateCarree(),zorder=0
             )
    return ax

def plot_dynamical_regions(ax,ocean_basins):
    counter=0
    colorbars=['white','cool','summer_r','summer','cyan']
    for ii in ocean_basins.data_vars:
        if 'processes' in ii:
            ocean_basins[ii].where(ocean_basins[ii]==True).plot.contourf(transform=ccrs.PlateCarree(),
                                                                     cmap=colorbars[counter],
                                                                     alpha=0.8,add_colorbar=False,
                                                                     vmin=0,vmax=1)
            counter+=1
    ax.set_global()

    ax.add_feature(ccrs_land, zorder=1)
    ax.spines['geo'].set_linewidth(1)

    ax.plot([1, 359], [9, 9],
             color='k', linewidth=0.5, linestyle='--',
             transform=ccrs.PlateCarree(),zorder=0
             )

    ax.plot([1, 359], [-9, -9],
             color='k', linewidth=0.5, linestyle='--',
             transform=ccrs.PlateCarree(),zorder=0
             )
    return ax

def compute_trends(data):
    slope, intercept, lslope, hslope = stats.mstats.theilslopes(data,range(len(data)),alpha=0.95)
    return slope,intercept

def significance_mk(data):
    h=np.zeros(np.shape(data)[0])
    n=np.zeros(np.shape(data)[0])
    ii=0
    mk_object = Mann_Kendall_test(data,'time',alpha=0.05,MK_modified=True,method="theilslopes")
    for item in data:
        result = mk_object._calc_slope_MK(item.values,effective_n=True)
        h[ii]=result[1]
        n[ii]=result[-1]
        ii+=1
    return h,n 
