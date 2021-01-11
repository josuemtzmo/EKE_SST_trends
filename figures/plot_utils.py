import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy as np

import cartopy.crs as ccrs
import cartopy.feature as feature


def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=100):
    new_cmap = colors.LinearSegmentedColormap.from_list(
        'trunc({n},{a:.2f},{b:.2f})'.format(n=cmap.name, a=minval, b=maxval),
        cmap(np.linspace(minval, maxval, n)))
    return new_cmap



import matplotlib.patches as mpatches

def add_patches(axis):
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