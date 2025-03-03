#!/usr/bin/env python3

import argparse
import xarray as xr
import rasterio as rio
import rioxarray 
import numpy as np
from scipy import ndimage
import os

def remove_outliers(array: xr.DataArray, std_dev_threshold: float = 3.0, filter_size: int = 3) -> xr.DataArray:
    """
    Remove outliers from an Xarray DataArray by applying a median filter.
    
    Parameters:
        array (xr.DataArray): Input DataArray with dimensions (x, y).
        std_dev_threshold (float): Number of standard deviations to use for outlier detection.
        filter_size (int): Size of the median filter kernel (default: 3x3).
    
    Returns:
        xr.DataArray: DataArray with outliers removed (set to NaN).
    """
    if filter_size <= 1:
        raise ValueError('filter size must greater than 1')
    # smooth array with median filter
    filtered = ndimage.median_filter(array, size=filter_size, mode="nearest")
    residuals = array - filtered
    std_dev = np.nanstd(residuals)
    # classify locations with residuals larger than threshold
    outliers = np.abs(residuals) > (std_dev_threshold*std_dev)
    # return array with outliers set to nan
    return array.where(~outliers)

def main():
    # set up argument parsing
    parser = argparse.ArgumentParser(description="Remove outliers from a DEM using a median filter.")
    
    parser.add_argument("dem_path", type=str, help="Path to the DEM file (GeoTIFF).")
    parser.add_argument("std_dev_threshold", type=float, help="Standard deviation threshold for outlier detection.")
    parser.add_argument("filter_size", type=int, help="Size of the median filter kernel.")

    args = parser.parse_args()

    # Load dem into xarray DataArray
    dem_da = rioxarray.open_rasterio(args.dem_path).squeeze()
    dem_da = dem_da.where(dem_da != 0)

    # perform outlier removal
    filtered_dem_da = remove_outliers(dem_da, args.std_dev_threshold, args.filter_size)

    # save output
    base, ext = os.path.splitext(args.dem_path)
    output_path = f"{base}_filtered{ext}"
    filtered_dem_da.rio.to_raster(output_path, compress='lzw')
    print(f"Processed DEM saved to {output_path}")

if __name__ == "__main__":
    main()
    