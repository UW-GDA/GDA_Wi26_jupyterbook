# 04: Raster 1 - Raster IO, basic properties, visualization, sampling, band math

UW Geospatial Data Analysis  
CEE467/CEWA567  
David Shean, Eric Gagliano, Quinn Brencher

Please quickly read through this entire document once, then go back and start tackling the various tasks.

## Overview
This week, we are going to cover raster basics. We will introduce and use `gdal`, `rasterio`, and `rioxarray` to process, analyze and visualize Landsat-8 satellite images over Washington state.



## Reading and Tutorials - *Complete before first Friday lab* (~2 hours)
Please review the following material, especially if you have limited GIS or remote sensing experience. If you are unfamiliar with any of the bulleted items, please make sure to google them before coming to class. At the very least, I'd like everyone to check out the links from parts 1 and 2, and also attempt part 3. 


### 1. Raster data properties

* [What is raster data?](https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/what-is-raster-data.htm)
    * Grid of cells / pixels containing values
* Raster structure
    * dimensions (width/columns and height/rows)
    * [bands](https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/raster-bands.htm)
        * [Introduction to Multispectral Remote Sensing Data in Python](https://www.earthdatascience.org/courses/use-data-open-source-python/multispectral-remote-sensing/intro-multispectral-data/)
    * data type (e.g. uint8, float32)
    * no data values (masked arrays vs. np.nan)

* Spatial properties
    * [resolution (pixel size)](https://desktop.arcgis.com/en/arcmap/latest/manage-data/raster-and-images/cell-size-of-raster-data.htm)
    * extent / geographic bounds
    * coordinate reference system (CRS)
        * pixel space 
            * integer coordinates, origin usually at the upper left
        * geographic space
            * projected coordinates (usually UTM)
            * transformation matrix
            * real world units (often meters)
            * floating point coordinates

* Storage
    * geotiff is most common raster file format
        * cloud optimized geotiff?
    * Many other formats via GDAL drivers
    * Compression options
    * overviews


### 2. Working with raster data

* Common operations
    * reading metadata
    * accessing pixel values
    * raster math and [band indicies](https://training.digitalearthafrica.org/en/latest/session_4/01_band_indices.html)
    * reprojection
    * mosaicing
    * orthorectification
    * clipping

* Common types of analysis and methods
    * qualitative / contextual analysis
    * spatial analysis
    * spectral analysis
    * time series analysis
    * change detection
    * aggregation and zonal statistics
    * machine learning / deep learning

* Memory management best practices
    * avoid loading large rasters entirely into memory
    * windowed & lazy reading
    * close datasets when finished


### 3. GDAL, rasterio, and rioxarray
Working with raster data is an essential part of geospatial analysis. There are several python packages available for raster processing, and we'll introduce three key tools that build on top of each other...

* GDAL (Geospatial Data Abstraction Library): The low-level foundation that powers most geospatial software. While powerful, it can be complex to use directly.
* rasterio: A more Pythonic interface to GDAL that provides efficient access to raster data using NumPy arrays.
* rioxarray: Higher-level package that combines the power of rasterio with xarray's labeled dimensions and advanced capabilities for handling multi-dimensional data. 

Each package plays an important role in the python geospatial ecosystem, so we'll briefly introduce the tools one at a time to practice some fundamentals and gain some raster intuition. 

*The lower level GDAL and rasterio are very well-supported, and there are indeed use cases for when you might prefer interacting with these lower level tools. Ultimately, we'll focus on rioxarray for the rest of the quarter due to its intuitive handling of multi-dimensional data (e.g. raster time series) and dask integration for scalability.*

We will run the data download demo all together on Monday. Before Wednesday, please run through the GDAL and rasterio demo notebooks and come to class on Wednesday with any questions. Make sure to close the tabs and kernels when you are done with each to reduce RAM usage and minimize crashes. We will go through the rioxarray demo notebook together in class on Wednesday.

## Assignment - *Due before class this Friday*
* Complete the above reading assignments
* Submit last week's lab assignment