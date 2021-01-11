import numpy as np

# Constant:
earth_radius = 6371e3
omega = 7.2921159e-5

# Function to compute grid area:
def area(lat,lon):
    lat_r = np.radians(lat)
    lon_r = np.radians(lon)
    f=2*omega*np.sin(lat_r)
    grad_lon=lon_r.copy()
    grad_lon.data=np.gradient(lon_r)

    dx=grad_lon*earth_radius*np.cos(lat_r)
    dy=np.gradient(lat_r)*earth_radius

    return dx*dy
    