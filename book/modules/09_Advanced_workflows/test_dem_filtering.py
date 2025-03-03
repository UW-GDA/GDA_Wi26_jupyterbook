import pytest
import numpy as np
import xarray as xr
from dem_filtering import remove_outliers

def test_remove_outliers():
    # Create a simple 5x5 test array with an outlier
    data = np.array([
        [1, 2, 2, 2, 1],
        [2, 1000, 2, 2, 2],  # 1000 is an outlier
        [2, 2, 2, 2, 2],
        [2, 2, 2, 2, 2],
        [1, 2, 2, 2, 1]
    ])
    
    da = xr.DataArray(data)

    # Run the function to detect the outlier
    filtered_da = remove_outliers(da, std_dev_threshold=2, filter_size=3)

    # Check if the outlier was set to NaN
    assert np.isnan(filtered_da[1, 1]), "Outlier was not removed"

    # Ensure non-outliers remain unchanged
    assert filtered_da[0, 0] == 1, "Unexpected value change"